
import array, re

class DataManager:
    def __init__(self):
        self._relics = {}


    def organize_data(self, _array : list) -> dict:
        relics_dict = self.relics_dictonary(_array)
        return self.sort_dictionary(relics_dict)


    def relics_dictonary(self, relics_array : list) -> dict: # Sort relics into dict
            
            relics_dict = {
                "Lith" : [],
                "Meso" : [],
                "Neo" : [],
                "Axi" : [],
                "Requiem" : []
            }

            for relic in relics_array:
                for key in relics_dict:
                    if relic.startswith(key):
                         relics_dict[key].append(relic)
            return relics_dict

    
    def sort_dictionary(self, relics_dict : dict) -> dict:
        for key in relics_dict:
             sorted_array = sorted(relics_dict[key], key=self.sort_combined)
             relics_dict[key] = sorted_array
        return relics_dict


    def sort_combined(self, relic : str): # Sorts primary & secondarr; p:letter, s:number
        match = re.search(r'([A-Z])(\d+)', relic)
        if match:
            letter = match.group(1)
            number = int(match.group(2))
            return (letter, number)
        else:
            return (relic, 0)
        
    
    def relic_count(self, relics_dict : dict) -> None: # Displays total relic count
        count = 0
        for key in relics_dict:
            for relic in relics_dict[key]:
                count += 1
            
        print(f"Total relic count: {count}")