__author__ = 'Krivenko'
from model.contact import Contact

def test_modify_contact_firstname(app):
        app.session.Login( username="admin", password="secret")
        app.contact.first_contact(Contact(firstname="Александр",
                            droplist="//div[@id='content']/form/select[1]//option[4]",
                            droplist2="//div[@id='content']/form/select[2]//option[8]",
                            droplist3="//div[@id='content']/form/select[3]//option[3]",droplist4="//div[@id='content']/form/select[4]//option[8]"))
        app.session.logout()

def test_modify_contact_user_middlename(app):
        app.session.Login( username="admin", password="secret")
        app.contact.first_contact(Contact(middlename="Михайлович",
                            droplist="//div[@id='content']/form/select[1]//option[4]",
                            droplist2="//div[@id='content']/form/select[2]//option[8]",
                            droplist3="//div[@id='content']/form/select[3]//option[3]",droplist4="//div[@id='content']/form/select[4]//option[8]"))
        app.session.logout()
