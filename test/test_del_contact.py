__author__ = 'Krivenko'
from model.contact import Contact
import random

def test_del_contact(app,db,check_ui):
        if len(db.get_contact_list())==0:
            app.contact.create_contact( Contact(firstname="Alex", middlename="a", lastname="Kriv", nickname="sd", title="fdf",
                                        company="sdd", address="we", homephone="we", mobilephone="433", workphone="443", fax="3",
                                        byear="1988", ayear="1988",address2="retert", phone2="rr", notes="e",
                                        droplist="//div[@id='content']/form/select[1]//option[4]",
                                        droplist2="//div[@id='content']/form/select[2]//option[8]",
                                        droplist3="//div[@id='content']/form/select[3]//option[3]",droplist4="//div[@id='content']/form/select[4]//option[8]"))
        old_list=db.get_contact_list()
        contact=random.choice(old_list)
        app.contact.delete_contact_by_id(contact.id)
        new_list=db.get_contact_list()
        #assert len(old_list) == len(new_list)
        old_list.remove(contact)
        assert len(old_list) == len(new_list)
        if check_ui:
            assert sorted(new_list,key=Contact.id_or_max) ==sorted(app.contact.get_contact_list(),key=Contact.id_or_max)
