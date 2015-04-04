# -*- coding: utf-8 -*-

from model.contact import Contact
import string
import random
import pytest
import re

def random_str(prefix,maxlen):
    symbols= string.ascii_letters + string.digits+' '*100
    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

test_data=[Contact(firstname='firstnameu', middlename='middle', lastname=random_str("lastname",10), nickname='nickname', title='title',
                                        company="sdd", address="we", homephone="500", mobilephone="433", workphone="443", fax="3",
                                        byear="1988", ayear="1988",address2="retert", phone2="rr", notes="e",
                                        droplist="//div[@id='content']/form/select[1]//option[4]",
                                        droplist2="//div[@id='content']/form/select[2]//option[8]",
                                        droplist3="//div[@id='content']/form/select[3]//option[3]",droplist4="//div[@id='content']/form/select[4]//option[8]") for i in range(1)]

@pytest.mark.parametrize('contact',test_data,ids=[repr(x) for x in test_data] )
def test_test_add_contact(app,contact):
     #app.open_home_page()
     old_list=app.contact.get_list()
     app.contact.create_contact(contact)
     new_list=app.contact.get_list()
     assert len(old_list)+1 == len(new_list)
     contact=del_spaces(contact)
     old_list.append(contact)
     assert sorted(old_list,key=Contact.id_or_max) == sorted(new_list,key=Contact.id_or_max)

def del_spaces(contact):
    contact.firstname=contact.firstname.replace(' ','')
    contact.lastname=contact.lastname.replace(' ','')
    return  contact