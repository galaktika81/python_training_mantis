
from model.project import Project

class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_projects_page(self):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-1.2.19/manage_proj_page.php")

    def create(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_css_selector("td.form-title > form > input.button-small").click()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_css_selector("input.button").click()
        wd.find_element_by_link_text("Proceed").click()

    def get_projects(self):
        wd = self.app.wd
        self.open_projects_page()
        projectsTable = wd.find_elements_by_xpath("//table[3]/tbody/tr")[2:]
        return [Project(name=p.find_element_by_xpath("td[1]").text) for p in projectsTable]

    def delete(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_link_text(project.name).click()
        wd.find_element_by_css_selector("form > input.button").click()
        wd.find_element_by_css_selector("input.button").click()