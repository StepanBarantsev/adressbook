from selenium import webdriver
import unittest
from model_contact import Contact

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(0)
        self.verificationErrors = []

    def test_add_contact(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, 'admin', 'secret')
        self.create_new_contact(driver, Contact(firstname='Stepan', middlename='Barantsev', lastname='Lol',
                                                nickname='Bloodes', email='stepan.barantsev@gmail.com'))
        self.logout(driver)


    def create_new_contact(self, driver, contact):
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("firstname").send_keys(contact.firstname)
        driver.find_element_by_name("middlename").send_keys(contact.middlename)
        driver.find_element_by_name("lastname").send_keys(contact.lastname)
        driver.find_element_by_name("nickname").send_keys(contact.nickname)
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(contact.email)
        driver.find_element_by_css_selector("input[name='submit']").click()
        driver.find_element_by_link_text("home page").click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def login(self, driver, name, password):      # Принимает логин и пароль.
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("user").send_keys(name)
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_css_selector("input[type='submit']").click()

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/")

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

if __name__ == "__main__":
    unittest.main()