# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
        app.Login( username="admin", password="secret")
        app.create( Group(name="k,kllk", header="yuyi", footer="hjh"))
        app.logout()

def test_add_empty_group(app):
        app.Login( username="admin", password="secret")
        app.create( Group(name="", header="", footer=""))
        app.logout()
