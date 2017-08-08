class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create_new_group(self, group):  # Создание группы. Принимает объект типа Group
        driver = self.app.driver
        driver.find_element_by_link_text("groups").click()
        driver.find_element_by_css_selector('input[name="new"]').click()
        self.input_group_fields(group)
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("group page").click()

    def delete_first_group(self): # Удаление группы
        driver = self.app.driver
        driver.find_element_by_link_text("groups").click()
        driver.find_element_by_css_selector('input[name="selected[]"]').click()
        driver.find_element_by_css_selector('input[name="delete"]').click()
        driver.find_element_by_link_text("group page").click()

    def modify_first_group(self, group): # Модификация группы. Принимает объект типа Group
        driver = self.app.driver
        driver.find_element_by_link_text("groups").click()
        driver.find_element_by_css_selector('input[name="selected[]"]').click()
        driver.find_element_by_css_selector('input[name="edit"]').click()
        self.input_group_fields(group)
        driver.find_element_by_name("update").click()
        driver.find_element_by_link_text("group page").click()


    def input_group_fields(self, group):   # Заполнение полей ввода. Принимает объект типа Group
        driver = self.app.driver
        driver.find_element_by_name("group_name").send_keys(group.group_name)
        driver.find_element_by_name("group_header").send_keys(group.group_header)
        driver.find_element_by_name("group_footer").send_keys(group.group_footer)