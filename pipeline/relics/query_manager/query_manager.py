


class QueryManager:
    def __init__(self):
        pass

    def relicQuery(self, relicData : dict) -> str:
        RELIC = ["Lith","Meso","Neo","Axi","Requiem"]
        ENTRY_STATEMENT = "INSERT INTO relics (Relic_Name, Type_ID)\nSELECT\n\tx.Relic_Name,\n\trt.Type_ID\nFROM ("
        CLOSING_STATEMENT = "\n) x\nJOIN relicType rt ON rt.Type_Name = x.Type_Name;"
        allRelics = []
        final = ""
        relicString = ""
        
        for type_index,type in enumerate(RELIC):
            for relic_index,relic in enumerate(relicData[type]):
                allRelics.append(relic)
                if type_index == 0 and relic_index == 0:
                    relicString += f"\n\tSELECT\n\t\t'{relic}' AS Relic_Name,\n\t\t'{type}' AS Type_Name"
                # if relic != "Requiem IV":
                #     relicString += f"\n\tUNION ALL SELECT '{relic}','{type}'"
                else:
                    relicString += f"\n\tUNION ALL SELECT '{relic}','{type}'"

        final += ENTRY_STATEMENT + relicString + CLOSING_STATEMENT
        return final, allRelics
    

    def contentQuery(self, contentData : dict, allRelics : list) -> str:
        RARITY = ["Common", "Uncommon", "Rare"]
        ENTRY_STATEMENT = "INSERT INTO relic_contents (Content_Name, Relic_ID, Rarity_ID, Type_ID)\nSELECT\n\tx.Content_Name,\n\tre.Relic_ID,\n\tra.Rarity_ID,\n\trt.Type_ID\nFROM ("
        CLOSING_STATEMENT = "\n) x\nJOIN relics re ON re.Relic_Name = x.Relic_Name\nJOIN rarity ra ON ra.Rarity_Name = x.Rarity_Name\nJOIN relicType rt ON rt.Type_Name = x.Type_Name;"
        final = ""
        contentString = ""

        for rel_index,relic in enumerate(allRelics):
            for rar_index,rarity in enumerate(RARITY):
                for con_index,content in enumerate(contentData[relic][rarity]):
                    _type = ""
                    for type_index,type in enumerate(["Lith","Meso","Neo","Axi","Requiem"]):
                        if type in relic:
                            _type = type
                            break
                    if rel_index == 0 and con_index == 0 and rar_index == 0:
                        contentString += f"\n\tSELECT\n\t\t'{content}' AS Content_Name,\n\t\t'{rarity}' AS Rarity_Name,\n\t\t'{relic}' AS Relic_Name,\n\t\t'{_type}' AS Type_Name"
                    else:
                        contentString += f"\n\tUNION ALL SELECT '{content}','{rarity}','{relic}','{type}'"


        final += ENTRY_STATEMENT + contentString + CLOSING_STATEMENT
        return final