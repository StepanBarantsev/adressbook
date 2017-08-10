from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def destroy(self):
        self.driver.quit()

    def open_home_page(self):
        driver = self.driver
        if not driver.current_url.endswith('/addressbook/'):
            driver.get("http://localhost/addressbook/")

    def is_valid(self):
        try:
            self.driver.current_url    # Если он может взять текущий url, то все в порядке.
            return True
        except:
            return False