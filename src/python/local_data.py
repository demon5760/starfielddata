import os
import yaml
import logging

class LocalData():
    systems_data_dir = "data/systems"
    planets_data_dir = "data/planets"
    moons_data_dir = "data/moons"

    BODY_CACHE = {}

    def __init__(self):
        pass

    def get_body(self, body_name):

        planet_file = "{}/{}.yaml".format(self.planets_data_dir, body_name)
        moon_file = "{}/{}.yaml".format(self.moons_data_dir, body_name)
        if self.BODY_CACHE.get(body_name, None) is None:
            if os.path.exists(planet_file):
                with open(planet_file, "r") as stream:
                    self.BODY_CACHE[body_name] = yaml.safe_load(stream)
            elif os.path.exists(moon_file):
                with open(moon_file, "r") as stream:
                    self.BODY_CACHE[body_name] = yaml.safe_load(stream)
                
        return self.BODY_CACHE.get(body_name)


    def get_system_names(self):
        results = []
        for file_name in os.listdir(self.systems_data_dir):
            results.append(file_name.replace(".yaml", ""))
        return results
    
    def get_planet_names(self, system_name):
        results = []
        for file_name in os.listdir(self.planets_data_dir):
            planet_name = file_name.replace(".yaml", "")
            planet = self.get_body(planet_name)
            if planet.get("system", None) == system_name:
                results.append(planet.get("name"))
        return results
    
    def get_moon_names(self, system_name):
        results = []
        for file_name in os.listdir(self.moons_data_dir):
            moon_name = file_name.replace(".yaml", "")
            moon = self.get_body(moon_name)
            planet = self.get_body(moon.get("planet"))
            if planet.get("system", None) == system_name:
                results.append(moon.get("name"))

        return results


    def get_system(self, system_name):
        """
        Load the system object from data file
        """
        if system_name == "ETA Cassiopeia":
            system_name = "Eta Cassiopeia"
        system_data_file = "{}/{}.yaml".format(self.systems_data_dir, system_name)
        with open(system_data_file, "r") as stream:
            return yaml.safe_load(stream)