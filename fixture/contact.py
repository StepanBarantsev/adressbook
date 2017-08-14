class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_new_contact(self, contact):         # Принимает объект типа Contact
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_element_by_link_text("add new").click()
        self.input_contact_fields(contact)
        driver.find_element_by_css_selector("input[name='submit']").click()
        driver.find_element_by_link_text("home page").click()

    def delete_first_contact(self):
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_element_by_name("selected[]").click()
        driver.find_element_by_css_selector("input[value='Delete']").click()
        driver.switch_to_alert().accept()
        driver.find_element_by_link_text("home").click()

    def input_contact_fields(self, contact):
        driver = self.app.driver
        if contact.firstname != None:
            driver.find_element_by_name("firstname").clear()
            driver.find_element_by_name("firstname").send_keys(contact.firstname)
        if contact.middlename != None:
            driver.find_element_by_name("middlename").clear()
            driver.find_element_by_name("middlename").send_keys(contact.middlename)
        if contact.lastname != None:
            driver.find_element_by_name("lastname").clear()
            driver.find_element_by_name("lastname").send_keys(contact.lastname)
        if contact.nickname != None:
            driver.find_element_by_name("nickname").clear()
            driver.find_element_by_name("nickname").send_keys(contact.nickname)
        if contact.email != None:
            driver.find_element_by_name("email").clear()
            driver.find_element_by_name("email").send_keys(contact.email)

    def modify_first_contact(self, contact):
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_element_by_css_selector('img[alt="Edit"]').click()
        self.input_contact_fields(contact)
        driver.find_element_by_css_selector('input[name="update"]').click()
        driver.find_element_by_link_text("home page").click()

    def count(self):
        driver = self.app.driver
        self.app.open_home_page()
        return len(driver.find_elements_by_name("selected[]"))

