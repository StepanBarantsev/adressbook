class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, name, password):      # Принимает логин и пароль.
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("user").send_keys(name)
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_css_selector("input[type='submit']").click()

    def logout(self):
        driver = self.app.driver
        driver.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        driver = self.app.driver
        if len(driver.find_elements_by_link_text("Logout")) > 0:
            self.logout()

    def ensure_login(self, name, password):
        driver = self.app.driver
        if len(driver.find_elements_by_link_text("Logout")) > 0:
            if self.is_logged_in_as(name):
                return
            else:
                self.logout()
        self.login(name, password)

    def is_logged_in_as(self, name):
        return self.get_logged_user() == name

    def get_logged_user(self):
        driver = self.app.driver
        return driver.find_element_by_xpath('//div/div[1]/form/b').text[1:-1]