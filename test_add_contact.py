# -*- coding: utf-8 -*-
import pytest
from application_contact import Application
from contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_test_add_contact(app):
    app.open_home_page()
    app.login()
    app.init_new_user()
    app.fill_user_form(Contact(firstname="Alex", middlename="a", lastname="Kriv", nickname="sd", title="fdf",
                                        company="sdd", address="we", home="we", mobile="433", work="443", fax="3",
                                        byear="1988", ayear="1988",
                                        address2="retert", phone2="rr", notes="e"),
                            "//div[@id='content']/form/select[1]//option[4]",
                            "//div[@id='content']/form/select[2]//option[8]")
    app.submit_user_creation()
    app.logout()

def test_test_add_empty_contact(app):
    app.open_home_page()
    app.login()
    app.init_new_user()
    app.fill_user_form( Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                                        address="", home="", mobile="", work="", fax="", byear="", ayear="",
                                        address2="", phone2="", notes=""),
                            droplist="//div[@id='content']/form/select[1]//option[4]",
                            droplist2="//div[@id='content']/form/select[2]//option[8]")
    app.submit_user_creation()
    app.logout()
