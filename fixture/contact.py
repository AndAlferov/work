
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_xpath("//table[@id='maintable']//a[.='Address']")) > 0):
            wd.find_element_by_xpath("//div/div[3]/ul/li[1]/a").click()

    def create(self, contact):
        wd = self.app.wd
        self.return_to_home_page()
        # init group creation
        wd.find_element_by_xpath("//div/div[3]/ul/li[2]/a").click()
        self.fill_contact_form(contact)
        # submit group
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.secondname)
        self.change_field_value("mobile", contact.number)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.return_to_home_page()
        self.edit_first_contact()
        # fill group form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def test_edit_first_contact(self):
        wd = self.app.wd
        self.edit_first_contact()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("EDIT")
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def edit_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("img[alt='Edit']").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div/div[3]/ul/li[1]/a").click()

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))
