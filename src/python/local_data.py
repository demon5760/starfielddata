import os
import yaml

class LocalData():
    systems_data_dir = "data/systems"
    planets_data_dir = "data/planets"
    moons_data_dir = "data/moons"

    def __init__(self):
        pass

    def get_body(self, body_name):

        planet_file = "{}/{}.yaml".format(self.planets_data_dir, body_name)
        moon_file = "{}/{}.yaml".format(self.moons_data_dir, body_name)
        if os.path.exists(planet_file):
            with open(planet_file, "r") as stream:
                return yaml.safe_load(stream)
        elif os.path.exists(moon_file):
            with open(moon_file, "r") as stream:
                return yaml.safe_load(stream)


    def get_system_names(self):
        results = []
        for file_name in os.listdir(self.systems_data_dir):
            results.append(file_name.replace(".yaml", ""))
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