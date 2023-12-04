"""
Compare the data we have locally against some other sources
so we know if we missed anything and/or have anything to
contribute back to those sources.
"""

import pandas as pd
import logging
from pprint import pprint
import sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

import local_data
from starfieldcompendium_checker import StarfieldCompendiumChecker


REPORT_TBD = False

class StarfieldSheetProcessor:
    SHEET_ID = "1idlpvoAhu2KHdi7J60Iz02HAIplHkEVpwt9JcmpWsKU"
    TAB_IDS = {
        'Stellar DB': "1413899096"
    }
    stellar_db_url = "https://docs.google.com/spreadsheets/export?id={}&exportFormat=csv&gid={}".format(SHEET_ID, TAB_IDS['Stellar DB'])

    def __init__(self):
        self.local_data = local_data.LocalData()
        self.stellar_db = pd.read_csv(self.stellar_db_url)
    
    def process(self):
        self.__compare_system_names()
        self.__compare_system_data()
        self.__compares_bodies()
        # logging.info(stellar_db.describe())

    def get_system_names(self):
        return self.stellar_db["System Name"].dropna().unique()
    
    def __compare_values(self, thing, attr_name, r_value, l_value):
        if isinstance(l_value, str):
            l_value = l_value.lower()
        if isinstance(r_value, str):
            r_value = r_value.lower()
            if r_value.startswith("std "):
                if l_value.startswith("standard "):
                    r_value = r_value.replace("std ", "standard ")

            if r_value.startswith("extr "):
                if l_value.startswith("extra "):
                    r_value = r_value.replace("extr ", "extra ")

        if attr_name == "Gravity":
            l_value = l_value.replace(" g", "")
            l_value = float(l_value)

        if r_value == "-":
            if l_value in ["-0", "none", 0]:
                return True
            
        if attr_name == "Traits":
            if pd.isnull(r_value):
                r_value = 0
            else:
              r_value = int(r_value)  
        
        if l_value == "tbd":
            # Not ready to chase these down just yet
            if not REPORT_TBD:
                return True
            
        if str(r_value) != str(l_value):
            logging.warning("{} has a different {}. Remote: '{}' Local: '{}'".format(thing, attr_name, r_value, l_value))
    
    def __compares_bodies(self):
        for index, row in self.stellar_db.iterrows():
            # Skip non-data rows
            if pd.isnull(row["System Name"]):
                continue
            system_name = row["System Name"]
            body_name = row["Location Name"]
            # Spelled wrong on the remote
            if body_name.startswith("Ursae M"):
                body_name = body_name.replace("Ursae M", "Ursa M")

            body = self.local_data.get_body(body_name)
            # logging.info("Comparing {} in {}.".format(body_name, system_name))

            self.__compare_values(body_name, "Type", row["Type"],  body["type"])
            self.__compare_values(body_name, "Gravity", row["Gravity"],  body["gravity"])
            self.__compare_values(body_name, "Temperature", row["Temperature"],  body["temperature"])
            self.__compare_values(body_name, "Atmosphere", row["Atmosphere"],  body["atmosphere"])
            self.__compare_values(body_name, "Magnetosphere", row["Magnetosphere"], body["magnetosphere"])
            self.__compare_values(body_name, "Water", row["Water"], body["water"])
            
            l_trait_count = len(body["traits"])
            if "Gravitational Anomaly" in body["traits"]:
                l_trait_count = len(body["traits"]) - 1
            self.__compare_values(body_name, "Traits", row["Traits"], l_trait_count)

            if row["Fauna"].lower().startswith("pri "):
                if body["fauna_rating"] != "Primordial":
                    logging.warning("Locally we have {} for Fauna rating for {}, but remote has pri so we should have Primordial.".format(body["fauna_rating"], body_name))
                self.__compare_values(body_name, "Fauna", row["Fauna"].lower().replace("pri ", ""), len(body["fauna"]))
            else:
                if body_name == "Zeta Ophiuchi VI-a":
                    print("wtf")
                    print(row["Fauna"])
                self.__compare_values(body_name, "Fauna", row["Fauna"], len(body["fauna"]))

            if row["Flora"].lower().startswith("pri "):
                if body["flora_rating"] != "Primordial":
                    logging.warning("Locally we have {} for Flora rating for {}, but remote has pri so we should have Primordial.".format(body["flora_rating"], body_name))
                self.__compare_values(body_name, "Flora", row["Flora"].lower().replace("pri ", ""), len(body["flora"]))
            else:
                self.__compare_values(body_name, "Flora", row["Flora"], len(body["flora"]))

    def __compare_system_data(self):
        for index, row in self.stellar_db.iterrows():
            if pd.isnull(row["System Name"]):
                continue
            ls = self.local_data.get_system(row["System Name"])

            r_level = row["System Level"]
            l_level = ls["level"]
            known_wrong = ["Ursae Majoris"]
            if row["System Name"] not in known_wrong:
                if r_level != l_level:
                    logging.warn("Different levels for {}. Remote: {} Local: {}".format(row["System Name"], r_level, l_level))


    def __compare_system_names(self):
        local_systems = self.local_data.get_system_names()
        remote_systems = self.get_system_names()
        if len(local_systems) == len(remote_systems):
            logging.info("Both sources contain {} systems".format(len(local_systems)))

        if sorted(local_systems) == sorted(remote_systems):
            logging.info("The system names in both sources match")
        else:
            remote_lower = [x.lower() for x in remote_systems]
            local_lower =  [x.lower() for x in local_systems]
            missing_from_local = list(set(remote_lower) - set(local_lower))
            missing_from_remote = list(set(local_lower) - set(remote_lower))
            if missing_from_local:
                logging.info("{} is in the remote source but missing from local".format(missing_from_local))
            if missing_from_remote:
                logging.info("{} is in the local source but missing from remote".format(missing_from_remote))

if __name__ == "__main__":
    logging.info("Checking Data")
    # StarfieldSheetProcessor().process()
    StarfieldCompendiumChecker().process()