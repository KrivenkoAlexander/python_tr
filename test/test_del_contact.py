__author__ = 'Krivenko'
from model.contact import Contact
from random import randrange

def test_del_contact(app):
        if app.contact.count()==0:
            app.contact.create_contact( Contact(firstname="Alex", middlename="a", lastname="Kriv", nickname="sd", title="fdf",
                                        company="sdd", address="we", homephone="we", mobilephone="433", workphone="443", fax="3",
                                        byear="1988", ayear="1988",address2="retert", phone2="rr", notes="e",
                                        droplist="//div[@id='content']/form/select[1]//option[4]",
                                        droplist2="//div[@id='content']/form/select[2]//option[8]",
                                        droplist3="//div[@id='content']/form/select[3]//option[3]",droplist4="//div[@id='content']/form/select[4]//option[8]"))
        old_list=app.contact.get_list()
        index=randrange(len(old_list))
        app.contact.delete_contact_by_index(index)
        new_list=app.contact.get_list()
        assert len(old_list)-1 == len(new_list)
        old_list[index:index+1]=[]
        assert len(old_list) == len(new_list)
