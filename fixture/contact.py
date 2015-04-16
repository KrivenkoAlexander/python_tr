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
        self.change_fields("home",contact.homephone)
        self.change_fields("mobile",contact.mobilephone)
        self.change_fields("work",contact.workphone)
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
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self,index):
        wd = self.app.wd
        self.open_contacts_page()
        #select  random contact
        wd.find_elements_by_name("selected[]")[index].click()
        # delete contact
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache=None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_id(self,contact,id):
        wd = self.app.wd
        self.open_contacts_page()
        self.open_contact_to_edit_by_id(id)
        # edit contacts field
        self.fill_user_form(contact)
        # submit changes of contact
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.open_contacts_page()
        self.contact_cache=None

    def modify_contact_by_index(self,contact,index):
        wd = self.app.wd
        self.open_contacts_page()
        self.open_contact_to_edit_by_index(index)
        # edit contacts field
        self.fill_user_form(contact)
        # submit changes of contact
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.open_contacts_page()
        self.contact_cache=None

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
        #self.open_contacts_page()
        wd.find_element_by_link_text("home").click()
        self.contact_cache=None

    contact_cache= None

    def get_list(self):
        wd=self.app.wd
        self.open_contacts_page()
        if  self.contact_cache is None:
            self.contact_cache=[]
            for contact in wd.find_elements_by_css_selector("tr[name=entry]"):
                cell=contact.find_elements_by_css_selector("td")
                firstname=cell[2].text#.replace(' ','')
                lastname=cell[1].text#.replace(' ','')
                id=contact.find_element_by_name("selected[]").get_attribute("value")
                allphones=cell[5].text
                allemail=cell[4].text
                alladress=cell[3].text
                self.contact_cache.append(Contact(lastname=lastname,firstname=firstname,id=id,allphones=allphones,allemail=allemail,alladress=alladress))
        return list(self.contact_cache)

    def get_contact_info_editpage(self,index):
        wd=self.app.wd
        self.open_contact_to_edit_by_index(index)
        # read information from fields
        firstname=wd.find_element_by_name('firstname').get_attribute('value')
        lastname=wd.find_element_by_css_selector('input[name=lastname]').get_attribute('value')
        id=wd.find_element_by_name('id').get_attribute('value')
        adress=wd.find_element_by_name("address").text
        homephone=wd.find_element_by_css_selector('input[name=home]').get_attribute('value')
        secondaryphone=wd.find_element_by_css_selector('input[name=phone2]').get_attribute('value')
        mobilephone=wd.find_element_by_css_selector('input[name=mobile]').get_attribute('value')
        workphone=wd.find_element_by_css_selector('input[name=work]').get_attribute('value')
        email=wd.find_element_by_css_selector('input[name=email]').get_attribute('value')
        email2=wd.find_element_by_css_selector('input[name=email2]').get_attribute('value')
        email3=wd.find_element_by_css_selector('input[name=email3]').get_attribute('value')
        contact= Contact(lastname=lastname,firstname=firstname,id=id,homephone=homephone,workphone=workphone,
                                mobilephone=mobilephone,secondaryphone=secondaryphone,email=email,email2=email2,email3=email3,address=adress)
        return contact

    def open_contact_to_edit_by_index(self,index):
        wd=self.app.wd
        self.open_contacts_page()
        tr=wd.find_elements_by_css_selector("tr[name=entry]")[index]
        tr.find_element_by_css_selector('img[alt=Edit]').click()

    def open_contact_to_edit_by_id(self,id):
        wd=self.app.wd
        self.open_contacts_page()
        self.select_contact_by_id(id)
       # tr_id=tr.find_element_by_css_selector("input[value='%s']"%id)
       # tr.find_element_by_css_selector('img[alt=Edit]').click()
        for tr in wd.find_elements_by_css_selector('tr[name=entry]'):
            if tr.find_element_by_css_selector("input[id='%s']"%id) == id:
                tr.find_element_by_css_selector('img[alt=Edit]').click()

    def get_contact_info_homepage(self,index):
        wd=self.app.wd
        self.open_contacts_page()
        contact=wd.find_elements_by_css_selector("tr[name=entry]")[index]
        cell=contact.find_elements_by_css_selector("td")
        firstname=cell[2].text
        lastname=cell[1].text
        id=contact.find_element_by_name("selected[]").get_attribute("value")
        allphones=cell[5].text
        allemail=cell[4].text
        alladress=cell[3].text
        contact= (Contact(lastname=lastname,firstname=firstname,id=id,allphones=allphones,allemail=allemail,alladress=alladress))
        return contact

    def select_contact_by_id(self,id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()


    def delete_contact_by_id(self,id):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_id(id)
        # delete contact
        wd.find_element_by_css_selector("input[value='Delete']").click()
        #wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache=None



