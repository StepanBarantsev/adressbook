# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from model_group import Group

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.verificationErrors = []

    def test_add_group(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, name='admin', password='secret')
        self.create_new_group(driver, Group(group_name='a', group_header='b', group_footer='c'))
        self.logout(driver)

    def test_add_empty_group(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, name='admin', password='secret')
        self.create_new_group(driver, Group(group_name='', group_header='', group_footer=''))
        self.logout(driver)

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def create_new_group(self, driver, group):  # Принимает фигню, которую можно забивать в группу.
        driver.find_element_by_link_text("groups").click()
        driver.find_element_by_css_selector('input[name="new"]').click()
        driver.find_element_by_name("group_name").send_keys(group.group_name)
        driver.find_element_by_name("group_header").send_keys(group.group_header)
        driver.find_element_by_name("group_footer").send_keys(group.group_footer)
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("group page").click()

    def login(self, driver, name, password):      # Принимает логин и пароль.
        driver.find_element_by_name("user").send_keys(name)
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_css_selector("input[type='submit']").click()

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
