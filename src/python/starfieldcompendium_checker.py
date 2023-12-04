import logging
import requests
from pprint import pprint

import local_data
from base_checker import BaseChecker

class StarfieldCompendiumChecker(BaseChecker):
    API_BASE_URL = "https://starfieldcompendium.com/api"
    CHECKER_NAME = "Starfield Compendium Checker"

    SYSTEMS_CACHED = None

    def get_remote_systems(self):
        if self.SYSTEMS_CACHED:
            return self.SYSTEMS_CACHED
        else:
            self.SYSTEMS_CACHED = requests.get(f"{self.API_BASE_URL}/Systems").json()
        
        return self.SYSTEMS_CACHED
    
    def get_remote_system_names(self):
        return [s['name'] for s in self.get_remote_systems()]
    
    def get_remote_system(self, system_name):
        # TODO - Explore if the API gives us a more direct way to do this
        for r_system in self.get_remote_systems():
            if r_system.get("name").upper() == system_name.upper():
                return r_system

    def get_remote_planet_names(self, system_name):
        results = []
        system = self.get_remote_system(system_name)
        for planet in system.get("sub"):
            results.append(planet.get("name"))
        return results
    
    def get_remote_moon_names(self, system_name):
        results = []
        system = self.get_remote_system(system_name)
        for planet in system.get("sub"):
            for moon in planet.get("sub"):
                results.append(moon.get("name"))
        return results




    