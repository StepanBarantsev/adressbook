from models.model_group import Group
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create_new_group(self, group):  # Создание группы. Принимает объект типа Group
        driver = self.app.driver
        self.open_groups_page()
        driver.find_element_by_css_selector('input[name="new"]').click()
        self.input_group_fields(group)
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("group page").click()

    def delete_first_group(self): # Удаление группы
        driver = self.app.driver
        self.open_groups_page()
        driver.find_element_by_css_selector('input[name="selected[]"]').click()
        driver.find_element_by_css_selector('input[name="delete"]').click()
        driver.find_element_by_link_text("group page").click()

    def modify_first_group(self, group): # Модификация группы. Принимает объект типа Group
        driver = self.app.driver
        self.open_groups_page()
        driver.find_element_by_css_selector('input[name="selected[]"]').click()
        driver.find_element_by_css_selector('input[name="edit"]').click()
        self.input_group_fields(group)
        driver.find_element_by_name("update").click()
        driver.find_element_by_link_text("group page").click()


    def input_group_fields(self, group):   # Заполнение полей ввода. Принимает объект типа Group
        driver = self.app.driver
        if group.group_name != None:
            driver.find_element_by_name("group_name").clear()
            driver.find_element_by_name("group_name").send_keys(group.group_name)
        if group.group_header != None:
            driver.find_element_by_name("group_header").clear()
            driver.find_element_by_name("group_header").send_keys(group.group_header)
        if group.group_footer != None:
            driver.find_element_by_name("group_footer").clear()
            driver.find_element_by_name("group_footer").send_keys(group.group_footer)

    def count(self):
        driver = self.app.driver
        self.open_groups_page()
        return len(driver.find_elements_by_css_selector('input[name="selected[]"]'))

    def open_groups_page(self):
        driver = self.app.driver
        if not(driver.current_url.endswith('/group.php') and len(driver.find_elements_by_name("new")) > 0):
            self.app.open_home_page()
            driver.find_element_by_link_text("groups").click()

    def get_group_list(self):
        driver = self.app.driver
        self.open_groups_page()
        groups = []
        for element in driver.find_elements_by_css_selector('span.group'):
            text = element.text
            element = element.find_element_by_css_selector('input[name="selected[]"]') # Это типа значит что надо искать элемент внутри element
            id = element.get_attribute('value')
            groups.append(Group(group_name=text, group_id=id))
        return groups