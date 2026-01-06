from manager.data_manager import DataManger
from manager.query_manager import QueryManager
from manager.export_manager import ExportManager



class Controller:
    def __init__(self):
        try:
            RELICS = "relics"
            RELICS_CONTENT = "relics-content"
            
            em = ExportManager()
            dm = DataManger()
            qm = QueryManager()
            
            relicData = em.getAssetData(RELICS)
            relicQuery, allRelics = qm.relicQuery(relicData)
            em.saveExportData(RELICS,relicQuery)

            # print(allRelics)

            contentData = em.getAssetData(RELICS_CONTENT)
            contentQuery = qm.contentQuery(contentData, allRelics)
            em.saveExportData(RELICS_CONTENT,contentQuery)

        except Exception as e:
            print(f"Exception: {e}")
        
        