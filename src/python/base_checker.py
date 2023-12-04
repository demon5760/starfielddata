import logging
from abc import ABC, abstractmethod

import local_data

class BaseChecker(ABC):

    def __init__(self):
        self.local_data = local_data.LocalData()

    @abstractmethod
    def get_remote_system_names(self):
        pass

    @abstractmethod
    def get_remote_planet_names(self, system_name):
        pass

    def get_local_planet_names(self, system_name):
        return self.local_data.get_planet_names(system_name)
    
    @abstractmethod
    def get_remote_moon_names(self, system_name):
        pass
    
    def get_local_moon_names(self, system_name):
        return self.local_data.get_moon_names(system_name)

    def get_local_system_names(self):
        return self.local_data.get_system_names()

    def process(self):
        logging.info(f"Running {self.CHECKER_NAME}.")
        self.compare_system_names()
        self.compare_planets()
        self.compare_moons()
        # print(self.get_local_planet_names("Cheyenne"))
        # print(self.get_local_moon_names("Cheyenne"))
        # print(self.get_remote_planet_names("Cheyenne"))
        # print(self.get_remote_moon_names("Cheyenne"))

    def _list_differ(self, local_items, remote_items):
        missing_from_local = list(set(remote_items) - set(local_items))
        missing_from_remote = list(set(local_items) - set(remote_items))
        return (missing_from_local, missing_from_remote)

    def compare_planets(self):
        for system_name in self.get_local_system_names():
            local = self.get_local_planet_names(system_name)
            remote = self.get_remote_planet_names(system_name)

            if len(local) != len(remote):
                logging.warn(f"Planet qty mismatch! Local: {len(local)} -- Remote: {len(remote)}.")
                missing_from_local, missing_from_remote = self._list_differ(local, remote)
                if missing_from_local:
                    logging.warn(f"Missing from local: {missing_from_local}")
                if missing_from_remote:
                    logging.warn(f"Missing from remote: {missing_from_remote}")

    def compare_moons(self):
        for system_name in self.get_local_system_names():
            local = self.get_local_moon_names(system_name)
            remote = self.get_remote_moon_names(system_name)

            if len(local) != len(remote):
                logging.warn(f"Moon qty mismatch! Local: {len(local)} -- Remote: {len(remote)}.")
                missing_from_local, missing_from_remote = self._list_differ(local, remote)
                if missing_from_local:
                    logging.warn(f"Missing from local: {missing_from_local}")
                if missing_from_remote:
                    logging.warn(f"Missing from remote: {missing_from_remote}")
    


    def compare_system_names(self):
        local_system_names = self.get_local_system_names()
        remote_system_names = self.get_remote_system_names()
        
        # Different data sources use different casing
        remote_upper = [x.upper() for x in remote_system_names]
        local_upper =  [x.upper() for x in local_system_names]

        # Remote source uses upper cases for system names where ours is using actual in-game casing
        if sorted(local_upper) == sorted(remote_upper):
            logging.info("The system names in both sources match")
        else:
            missing_from_local = list(set(remote_system_names) - set(local_system_names))
            missing_from_remote = list(set(local_system_names) - set(remote_system_names))
            if missing_from_local:
                logging.info(f"Missing from Local: {missing_from_local}")
            if missing_from_remote:
                logging.info(f"Missing from Remote: {missing_from_remote}")