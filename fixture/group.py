__author__ = 'Krivenko'

class GroupHelper:

    def __init__(self,app):
        self.app=app

    def Open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self,group):
        wd = self.app.wd
        self.Open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.Open_groups_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion group
        wd.find_element_by_name("delete").click()
        self.return_groups_page()

    def edit_group(self,group):
        wd = self.app.wd
        # select group
        wd.find_element_by_name("selected[]").click()
        #click on edit button
        wd.find_element_by_name("edit").click()
        # changing fields
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # update group
        wd.find_element_by_name("update").click()
        # back to groups page
        self.return_groups_page()


    def return_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()