# -*- coding: utf-8 -*-

from model.contact import Contact

def test_test_add_contact(app,db,json_contacts,check_ui):
     contact=json_contacts
     app.open_home_page()
     old_list=db.get_contact_list()
     app.contact.create_contact(contact)
     new_list=db.get_contact_list()
     old_list.append(contact)
     assert sorted(old_list,key=Contact.id_or_max) == sorted(new_list,key=Contact.id_or_max)
     if check_ui:
         assert sorted(new_list,key=Contact.id_or_max) ==sorted(app.contact.get_contact_list(),key=Contact.id_or_max)

def del_spaces(contact):

    contact.firstname=contact.firstname.replace(' ','')
    contact.lastname=contact.lastname.replace(' ','')
    return  contact