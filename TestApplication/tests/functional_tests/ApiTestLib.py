import requests
from pprint import pprint

class ApiTestLib:
    def get_tasks(self,url, api):
        rs = requests.get("%s%s"%(url,api))
        pprint(rs.status_code)
        assert rs.status_code == 200
        # logger.info(rs.json())
        pprint(rs.json())


