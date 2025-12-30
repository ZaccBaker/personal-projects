import array, re
from util.toLinkName import toLinkName

class DataManager:
    def __init__(self):
        self._relics = {}


    def planet_dictonary(planet_array : list) -> dict:
        
        planet_dict = {}

        for planet in planet_array:
                planet_dict.update({planet:False})
        return planet_dict


    def planet_address(planet_array : list) -> list:
        new_array = []
        for planet in planet_array:
            if planet == "Zariman":
                new_array.append("Zariman_Ten_Zero")
            else:
                new_array.append(toLinkName(planet))
        return new_array
    

    def starchart_dictonary(planet : str, mission_array : list):
        
        new_dict = {
                "Name" : [],
                "Type" : []
        }

        for pair in mission_array:
            new_dict["Name"].append(pair[0])
            new_dict["Type"].append(pair[1])

        return new_dict