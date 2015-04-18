__author__ = 'Krivenko'
from model.contact import Contact
from random import randrange

def test_modify_contact_firstname(app,db,check_ui):
    if app.contact.count()==0:
        app.contact.create_contact( Contact(firstname="Alex", middlename="a", lastname="Kriv", nickname="sd", title="fdf",
                                        company="sdd", address="we", homephone="we", mobilephone="433", workphone="443", fax="3",
                                        byear="1988", ayear="1988",address2="retert", phone2="rr", notes="e",
                                        droplist="//div[@id='content']/form/select[1]//option[4]",
                                        droplist2="//div[@id='content']/form/select[2]//option[8]",
                                        droplist3="//div[@id='content']/form/select[3]//option[3]",droplist4="//div[@id='content']/form/select[4]//option[8]"))
    old_list=db.get_contact_list()
    index=randrange(len(old_list))
    contact_data=Contact(firstname="Александр",
                            droplist="//div[@id='content']/form/select[1]//option[4]",
                            droplist2="//div[@id='content']/form/select[2]//option[8]",
                            droplist3="//div[@id='content']/form/select[3]//option[3]",droplist4="//div[@id='content']/form/select[4]//option[8]")
    contact_data.id=old_list[index].id
    app.contact.modify_contact_by_id(contact_data,contact_data.id)
    new_list=db.get_contact_list()
    old_list[index]=contact_data
    assert sorted(old_list,key=Contact.id_or_max) == sorted(new_list,key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_list,key=Contact.id_or_max) == sorted(app.contact.get_contact_list,key=Contact.id_or_max)




# old_list=app.contact.get_list()
 #   index=randrange(len(old_list))
 #   contact_data=Contact(firstname="Александр",
 #                           droplist="//div[@id='content']/form/select[1]//option[4]",
 #                           droplist2="//div[@id='content']/form/select[2]//option[8]",
 #                           droplist3="//div[@id='content']/form/select[3]//option[3]",droplist4="//div[@id='content']/form/select[4]//option[8]")
 #   contact_data.id=old_list[index].id
 #   app.contact.modify_contact_by_index(contact_data,index)
 #   new_list=app.contact.get_list()
 #  assert len(old_list) == len(new_list)
 #  old_list[index]=contact_data
 #  assert sorted(old_list,key=Contact.id_or_max) == sorted(new_list,key=Contact.id_or_max)
