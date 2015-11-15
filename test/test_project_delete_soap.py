from model.project import Project
import random
from generator.random import random_string


def test_project_delete(app):
    project = None

    old_projects = app.soap.get_projects()
    if len(old_projects) == 0:
        project = Project(name=random_string("PN", 20))
        app.soap.create( project)
        old_projects.append(project)
    else:
        project = random.choice(old_projects)

    app.soap.delete(project)

    new_projects = app.soap.get_projects()
    old_projects.remove(project)

    assert len(old_projects) == len(new_projects)
    assert sorted(old_projects, key=Project.Key) == sorted(new_projects, key=Project.Key)
