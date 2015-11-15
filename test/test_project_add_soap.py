from model.project import Project
from generator.random import random_string


def test_project_add(app):
    old_projects = app.soap.get_projects()
    project = Project(name=random_string("PN", 20))
    app.soap.create(project)

    new_projects = app.soap.get_projects()
    old_projects.append(project)

    assert len(old_projects) == len(new_projects)
    assert sorted(old_projects, key=Project.Key) == sorted(new_projects, key=Project.Key)
