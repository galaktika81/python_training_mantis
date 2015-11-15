__author__ = 'cyhis'

from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:
    def __init__(self, app):
        self.app = app
        self.username = self.app.config['webadmin']['username']
        self.password = self.app.config['webadmin']['password']

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.19/api/soap/mantisconnect.php?wsdl")

        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def create(self, project):
        client = Client("http://localhost/mantisbt-1.2.19/api/soap/mantisconnect.php?wsdl")

        try:
            pData = client.factory.create('ProjectData')
            pData.name = project.name
            client.service.mc_project_add(self.username, self.password, pData)
            return True
        except WebFault:
            return False

    def get_projects(self):
        client = Client("http://localhost/mantisbt-1.2.19/api/soap/mantisconnect.php?wsdl")

        projects = []
        try:
            projectsData = client.service.mc_projects_get_user_accessible(self.username, self.password)
            for projectData in projectsData:
                project = Project(name=projectData['name'])
                projects.append(project)
            return projects
        except WebFault:
            return False

    def delete(self, project):
        client = Client("http://localhost/mantisbt-1.2.19/api/soap/mantisconnect.php?wsdl")

        try:
            projectsData = client.service.mc_projects_get_user_accessible(self.username, self.password)
            for projectData in projectsData:
                if projectData['name'] == project.name:
                    client.service.mc_project_delete(self.username, self.password, projectData['id'])
                    return True
        except WebFault:
            return False