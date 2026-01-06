


class QueryManager:
    def __init__(self):
        pass

    def relicQuery(self, relicData : dict) -> str:
        RELIC = ["Lith","Meso","Neo","Axi","Requiem"]
        ENTRY_STATEMENT = "INSERT INTO relics (Relic_Name)\nVALUES"
        allRelics = []
        final = ""
        relicString = ""
        
        for r in RELIC:
            for relic in relicData[r]:
                allRelics.append(relic)
                if relic != "Requiem IV":
                    relicString += f"\n\t('{relic}'),"
                else:
                    relicString += f"\n\t('{relic}');"

        final += ENTRY_STATEMENT + relicString
        return final, allRelics
    

    def contentQuery(self, contentData : dict, allRelics : list) -> str:
        RARITY = ["Common", "Uncommon", "Rare"]
        ENTRY_STATEMENT = "INSERT INTO relic_contents (Content_Name, Relic_ID, Rarity_ID)\nSELECT\n\tx.Content_Name,\n\tre.Relic_ID,\n\tra.Rarity_ID\nFROM ("
        CLOSING_STATEMENT = "\n) x\nJOIN relics re ON re.Relic_Name = x.Relic_Name\nJOIN rarity ra ON ra.Rarity_Name = x.Rarity_Name;"
        final = ""
        contentString = ""

#         test = f"""
#             \n\tSELECT\n\t\t{content} AS Content_Name,\n\t\t{rarity} AS Rarity_Name,\n\t\t{relic} AS Relic_Name

# """

        for rel_index,relic in enumerate(allRelics):
            for rar_index,rarity in enumerate(RARITY):
                for con_index,content in enumerate(contentData[relic][rarity]):
                    if rel_index == 0 and con_index == 0 and rar_index == 0:
                        contentString += f"\n\tSELECT\n\t\t'{content}' AS Content_Name,\n\t\t'{rarity}' AS Rarity_Name,\n\t\t'{relic}' AS Relic_Name"
                    else:
                        contentString += f"\n\tUNION ALL SELECT '{content}','{rarity}','{relic}'"


        final += ENTRY_STATEMENT + contentString + CLOSING_STATEMENT
        return final