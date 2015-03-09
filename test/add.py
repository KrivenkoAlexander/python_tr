# -*- coding: utf-8 -*-

from model.group import Group

def test_add_group(app):
        app.session.Login( username="admin", password="secret")
        app.group.create( Group(name="k,kllk", header="yuyi", footer="hjh"))
        app.session.logout()

def test_add_empty_group(app):
        app.session.Login( username="admin", password="secret")
        app.group.create( Group(name="", header="", footer=""))
        app.session.logout()
