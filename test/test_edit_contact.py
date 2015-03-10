__author__ = 'Krivenko'
from model.contact import Contact

def test_edit_contact(app):
        app.session.Login( username="admin", password="secret")
        app.contact.edit(Contact(firstname="Александр", middlename="Михайлович", lastname="Кривенко", nickname="фы", title="вау",
                                        company="уу", address="ккк", home="www", mobile="ee", work="ww", fax="e",
                                        byear="1987", ayear="1989",
                                        address2="rrrwrt", phone2="rwu", notes="бь"),
                            "//div[@id='content']/form/select[1]//option[4]",
                            "//div[@id='content']/form/select[2]//option[8]")
        app.session.logout()