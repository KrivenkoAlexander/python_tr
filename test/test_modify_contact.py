__author__ = 'Krivenko'
from model.contact import Contact

def test_modify_contact_firstname(app):
    if app.contact.count()==0:
        app.contact.create_contact( Contact(firstname="Alex", middlename="a", lastname="Kriv", nickname="sd", title="fdf",
                                        company="sdd", address="we", home="we", mobile="433", work="443", fax="3",
                                        byear="1988", ayear="1988",address2="retert", phone2="rr", notes="e",
                                        droplist="//div[@id='content']/form/select[1]//option[4]",
                                        droplist2="//div[@id='content']/form/select[2]//option[8]",
                                        droplist3="//div[@id='content']/form/select[3]//option[3]",droplist4="//div[@id='content']/form/select[4]//option[8]"))
    old_list=app.contact.get_list()
    app.contact.modify_first_contact(Contact(firstname="Александр",
                            droplist="//div[@id='content']/form/select[1]//option[4]",
                            droplist2="//div[@id='content']/form/select[2]//option[8]",
                            droplist3="//div[@id='content']/form/select[3]//option[3]",droplist4="//div[@id='content']/form/select[4]//option[8]"))
    new_list=app.contact.get_list()
    assert len(old_list) == len(new_list)

def test_modify_contact_user_middlename(app):
    if app.contact.count()==0:
        app.contact.create_contact( Contact(firstname="Alex", middlename="a", lastname="Kriv", nickname="sd", title="fdf",
                                        company="sdd", address="we", home="we", mobile="433", work="443", fax="3",
                                        byear="1988", ayear="1988",address2="retert", phone2="rr", notes="e",
                                        droplist="//div[@id='content']/form/select[1]//option[4]",
                                        droplist2="//div[@id='content']/form/select[2]//option[8]",
                                        droplist3="//div[@id='content']/form/select[3]//option[3]",droplist4="//div[@id='content']/form/select[4]//option[8]"))
    old_list=app.contact.get_list()
    app.contact.modify_first_contact(Contact(middlename="Михайлович",
                            droplist="//div[@id='content']/form/select[1]//option[4]",
                            droplist2="//div[@id='content']/form/select[2]//option[8]",
                            droplist3="//div[@id='content']/form/select[3]//option[3]",droplist4="//div[@id='content']/form/select[4]//option[8]"))
    new_list=app.contact.get_list()
    assert len(old_list) == len(new_list)

