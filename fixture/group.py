class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create_new_group(self, group):  # Принимает объекти типа Group
        driver = self.app.driver
        driver.find_element_by_link_text("groups").click()
        driver.find_element_by_css_selector('input[name="new"]').click()
        driver.find_element_by_name("group_name").send_keys(group.group_name)
        driver.find_element_by_name("group_header").send_keys(group.group_header)
        driver.find_element_by_name("group_footer").send_keys(group.group_footer)
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("group page").click()