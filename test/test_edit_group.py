__author__ = 'Krivenko'
from model.group import Group

def test_edit_group(app):
        app.session.Login( username="admin", password="secret")
        # open groups page
        app.group.Open_groups_page()
        # edit group and update
        app.group.edit_group(Group(name="раз", header="два", footer="три"))
        # log out
        app.session.logout()