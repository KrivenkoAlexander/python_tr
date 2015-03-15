__author__ = 'Krivenko'
from model.group import Group

def test_modify_group_name(app):
        # open groups page
        app.group.Open_groups_page()
        if app.group.count()==0:
            app.group.create(Group(name="test"))
        # edit group and update
        app.group.modify_first_group(Group(name="New name"))

def test_modify_group_header(app):
        # open groups page
        app.group.Open_groups_page()
        if app.group.count()==0:
            app.group.create(Group(name="test",header="test"))
        # edit group and update
        app.group.modify_first_group(Group(header="New header"))