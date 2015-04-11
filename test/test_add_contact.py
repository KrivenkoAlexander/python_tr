# -*- coding: utf-8 -*-

from model.contact import Contact

def test_test_add_contact(app,json_contacts):
     contact=json_contacts
     app.open_home_page()
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