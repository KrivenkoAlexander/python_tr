__author__ = 'Krivenko'

class GroupHelper:

    def __init__(self,app):
        self.app=app

    def Open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def change_field_val(self,field_name,text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_val("group_name",group.name)
        self.change_field_val("group_header",group.header)
        self.change_field_val("group_footer",group.footer)

    def create(self,group):
        wd = self.app.wd
        self.Open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.Open_groups_page()
        self.select_first_group()
        # submit deletion group
        wd.find_element_by_name("delete").click()
        self.return_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_group(self,new_group_data):
        wd = self.app.wd
        self.select_first_group()
        #open modification form
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        # update group
        wd.find_element_by_name("update").click()
        # back to groups page
        self.return_groups_page()


    def return_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()