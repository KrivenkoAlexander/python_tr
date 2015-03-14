# -*- coding: utf-8 -*-

from model.contact import Contact

def test_test_add_contact(app):
    app.open_home_page()
    app.contact.init_new_user()
    app.contact.fill_user_form(Contact(firstname="Alex", middlename="a", lastname="Kriv", nickname="sd", title="fdf",
                                        company="sdd", address="we", home="we", mobile="433", work="443", fax="3",
                                        byear="1988", ayear="1988",
                                        address2="retert", phone2="rr", notes="e"),
                            "//div[@id='content']/form/select[1]//option[4]",
                            "//div[@id='content']/form/select[2]//option[8]")
    app.contact.submit_user_creation()

def test_test_add_empty_contact(app):
    app.open_home_page()
    app.contact.init_new_user()
    app.contact.fill_user_form( Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                                        address="", home="", mobile="", work="", fax="", byear="", ayear="",
                                        address2="", phone2="", notes=""),
                            droplist="//div[@id='content']/form/select[1]//option[4]",
                            droplist2="//div[@id='content']/form/select[2]//option[8]")
    app.contact.submit_user_creation()