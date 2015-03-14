__author__ = 'Krivenko'
from model.group import Group

def test_modify_group_name(app):
        app.session.Login( username="admin", password="secret")
        # open groups page
        app.group.Open_groups_page()
        # edit group and update
        app.group.modify_first_group(Group(name="New name"))
        # log out
        app.session.logout()

def test_modify_group_header(app):
        app.session.Login( username="admin", password="secret")
        # open groups page
        app.group.Open_groups_page()
        # edit group and update
        app.group.modify_first_group(Group(header="New header"))
        # log out
        app.session.logout()