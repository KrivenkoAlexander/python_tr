# -*- coding: utf-8 -*-

from model.contact import Contact

def test_test_add_contact(app):
    app.open_home_page()
    old_list=app.contact.get_list()
    contact= Contact(firstname="Alex", middlename="a", lastname="Kriv", nickname="sd", title="fdf",
                                        company="sdd", address="we", home="we", mobile="433", work="443", fax="3",
                                        byear="1988", ayear="1988",address2="retert", phone2="rr", notes="e",
                                        droplist="//div[@id='content']/form/select[1]//option[4]",
                                        droplist2="//div[@id='content']/form/select[2]//option[8]",
                                        droplist3="//div[@id='content']/form/select[3]//option[3]",droplist4="//div[@id='content']/form/select[4]//option[8]")
    app.contact.create_contact(contact)
    new_list=app.contact.get_list()
    assert len(old_list)+1 == len(new_list)
    old_list.append(contact)
    assert sorted(old_list,key=Contact.id_or_max) == sorted(new_list,key=Contact.id_or_max)

#def test_test_add_empty_contact(app):
#    app.open_home_page()
#    old_list=app.contact.get_list()
#    app.contact.create_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
#                                        address="", home="", mobile="", work="", fax="", byear="", ayear="",
#                                        address2="", phone2="", notes="",
#                                        droplist="//div[@id='content']/form/select[1]//option[4]",
#                                        droplist2="//div[@id='content']/form/select[2]//option[8]",
#                                        droplist3="//div[@id='content']/form/select[3]//option[3]",droplist4="//div[@id='content']/form/select[4]//option[8]"))
#    new_list=app.contact.get_list()
#    assert len(old_list)+1 == len(new_list)