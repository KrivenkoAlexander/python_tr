__author__ = 'Krivenko'

def test_del_group(app):
        app.session.Login( username="admin", password="secret")
        app.group.delete_first_group()
        app.session.logout()