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

