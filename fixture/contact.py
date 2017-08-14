from models.model_contact import Contact
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
        self.cont_cashe = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

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
        self.modify_contact_by_index(contact, 0)

    def count(self):
        driver = self.app.driver
        self.app.open_home_page()
        return len(driver.find_elements_by_name("selected[]"))

    cont_cashe = None

    def get_contact_list(self):
        if self.cont_cashe == None:
            driver = self.app.driver
            self.app.open_home_page()
            self.cont_cashe = []
            for element in driver.find_elements_by_css_selector('tr[name="entry"]'):
                id = element.find_element_by_css_selector('input[name="selected[]"]').get_attribute('value')
                text = list(element.text.split())
                firstname = text[1]
                lastname = text[0]
                self.cont_cashe.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return list(self.cont_cashe)

    def delete_contact_by_index(self, index):
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_elements_by_name("selected[]")[index].click()
        driver.find_element_by_css_selector("input[value='Delete']").click()
        driver.switch_to_alert().accept()
        driver.find_element_by_link_text("home").click()
        self.cont_cashe = None

    def modify_contact_by_index(self, contact, index):
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_elements_by_css_selector('img[alt="Edit"]')[index].click()
        self.input_contact_fields(contact)
        driver.find_element_by_css_selector('input[name="update"]').click()
        driver.find_element_by_link_text("home page").click()
        self.cont_cashe = None