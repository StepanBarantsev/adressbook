class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_new_contact(self, contact):         # Принимает объекти типа Contact
        driver = self.app.driver
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("firstname").send_keys(contact.firstname)
        driver.find_element_by_name("middlename").send_keys(contact.middlename)
        driver.find_element_by_name("lastname").send_keys(contact.lastname)
        driver.find_element_by_name("nickname").send_keys(contact.nickname)
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(contact.email)
        driver.find_element_by_css_selector("input[name='submit']").click()
        driver.find_element_by_link_text("home page").click()