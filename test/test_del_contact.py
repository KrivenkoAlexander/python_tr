__author__ = 'Krivenko'
from model.contact import Contact

def test_del_contact(app):
        if app.contact.count()==0:
            app.contact.create_contact( Contact(firstname="Alex", middlename="a", lastname="Kriv", nickname="sd", title="fdf",
                                        company="sdd", address="we", home="we", mobile="433", work="443", fax="3",
                                        byear="1988", ayear="1988",address2="retert", phone2="rr", notes="e",
                                        droplist="//div[@id='content']/form/select[1]//option[4]",
                                        droplist2="//div[@id='content']/form/select[2]//option[8]",
                                        droplist3="//div[@id='content']/form/select[3]//option[3]",droplist4="//div[@id='content']/form/select[4]//option[8]"))
        old_list=app.contact.get_list()
        app.contact.delete_first_contact()
        new_list=app.contact.get_list()
        assert len(old_list)-1 == len(new_list)
        old_list[0:1]=[]
        assert len(old_list) == len(new_list)
