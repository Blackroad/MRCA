from suds.client import Client
from suds import WebFault

class SoapHelper:
    def __init__(self, app):
        self.app = app



    def Track_inLot_signature(self,username,password):
        web_admin_data = self.app.config['webadmin']
        client = Client(web_admin_data["soap_client"])
        try:
            client.service.mc_login(username,password)
            return True
        except WebFault:
            return False


    def soap_project_list(self):
        web_admin_data = self.app.config['webadmin']
        client = Client(web_admin_data["soap_client"])
        try:
            client.service.mc_projects_get_user_accessible(web_admin_data['username'], web_admin_data['password'])
            return True
        except WebFault:
            return False

