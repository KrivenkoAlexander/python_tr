__author__ = 'Krivenko'
from model.contact import Contact

class ContactHelper:

    def __init__(self,app):
        self.app = app

    def init_new_user(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def change_fields(self,field_name,text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_drop_list(self, droplist):
        wd = self.app.wd
        if  wd.find_element_by_xpath(droplist).is_selected():
            pass

    def fill_user_form(self,contact):
        wd = self.app.wd
        self.change_fields("firstname",contact.firstname)
        self.change_fields("middlename",contact.middlename)
        self.change_fields("lastname",contact.lastname)
        self.change_fields("nickname",contact.nickname)
        self.change_fields("title",contact.title)
        self.change_fields("company",contact.company)
        self.change_fields("address",contact.address)
        self.change_fields("home",contact.home)
        self.change_fields("mobile",contact.mobile)
        self.change_fields("work",contact.work)
        self.change_fields("fax",contact.fax)
        self.select_drop_list(contact.droplist)
        self.select_drop_list(contact.droplist2)
        self.change_fields("byear",contact.byear)
        self.select_drop_list(contact.droplist3)
        self.select_drop_list(contact.droplist4)
        self.change_fields("ayear",contact.ayear)
        self.change_fields("address2",contact.address2)
        self.change_fields("phone2",contact.phone2)
        self.change_fields("notes",contact.notes)

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contacts_page()
        #select  the first contact
        wd.find_element_by_name("selected[]").click()
        # delete contact
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self,contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_first_contact()
        # pick on edit button
        wd.find_element_by_xpath("//div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()
        # edit contacts field
        self.fill_user_form(contact)
        # submit changes of contact
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.open_contacts_page()

    def submit_user_creation(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def open_contacts_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/addressbook") and len(wd.find_elements_by_link_text("Last name"))>0):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    def create_contact(self,contact_data):
        wd = self.app.wd
        self.init_new_user()
        self.fill_user_form(contact_data)
        self.submit_user_creation()
        self.open_contacts_page()

    def get_list(self):
        wd=self.app.wd
        self.open_contacts_page()
        list_contact=[]
        for contact in wd.find_elements_by_css_selector("tr[name=entry]"):
            text=contact.text
            id=contact.find_element_by_name("selected[]").get_attribute("value")
            list_contact.append(Contact(firstname=text,id=id))
        return list_contact
