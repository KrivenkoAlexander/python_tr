# -*- coding: utf-8 -*-
__author__ = 'Krivenko'
from model.contact import Contact
from random import randrange
import re


def test_check_contact(app):
    if app.contact.count()==0:
        app.contact.create_contact( Contact(firstname="Alex", middlename="a", lastname="Kriv", nickname="sd", title="fdf",
                                        company="sdd", address="we", homephone="we", mobilephone="433", workphone="443", fax="3",
                                        byear="1988", ayear="1988",address2="retert", phone2="rr", notes="e",
                                        droplist="//div[@id='content']/form/select[1]//option[4]",
                                        droplist2="//div[@id='content']/form/select[2]//option[8]",
                                        droplist3="//div[@id='content']/form/select[3]//option[3]",droplist4="//div[@id='content']/form/select[4]//option[8]"))
    old_list=app.contact.get_contact_list()
    index=randrange(len(old_list))
    con1= app.contact.get_contact_info_homepage(index)
    con2=app.contact.get_contact_info_editpage(index)
    assert con1.firstname == con2.firstname
    assert con1.lastname == con2.lastname
    assert con1.id == con2.id
    assert  con1.alladress == merge_adress_like_on_home_page(con2)
    assert  con1.allemail == merge_email_like_on_home_page(con2)
    assert  con1.allphones == merge_phones_like_on_home_page(con2)


def clear(s):
    return re.sub("[ () / -]","",s)

def  merge_phones_like_on_home_page(con2):
    return "\n".join(filter(lambda x:x!="",
                           map(lambda x:clear(x),
                               filter(lambda x:x is not None,[con2.homephone,con2.mobilephone,con2.workphone,con2.secondaryphone]))))

def  merge_email_like_on_home_page(con2):
    return "\n".join(filter(lambda x:x!="",
                               filter(lambda x:x is not None,[con2.email,con2.email2,con2.email3])))

def  merge_adress_like_on_home_page(con2):
    return "\n".join(filter(lambda x:x!="",
                               filter(lambda x:x is not None,con2.address.split())))
