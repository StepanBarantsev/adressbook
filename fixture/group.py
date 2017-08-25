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
        self.group_cashe = None   # Тут кеш сбрасываем, так как списко изменен

    def delete_first_group(self): # Удаление группы
        self.delete_group_by_index(0)

    def modify_first_group(self): # Модификация группы. Принимает объект типа Group
        self.modify_group_by_index(0)

    def input_group_fields(self, group):  # Заполнение полей ввода. Принимает объект типа Group
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

    group_cashe = None

    def get_group_list(self):
        if self.group_cashe == None:    # Тут если что то уже лежит в кеше, то все отлично
            driver = self.app.driver
            self.open_groups_page()
            self.groups_cashe = []
            for element in driver.find_elements_by_css_selector('span.group'):
                text = element.text
                element = element.find_element_by_css_selector('input[name="selected[]"]') # Это типа значит что надо искать элемент внутри element
                id = element.get_attribute('value')
                self.groups_cashe.append(Group(group_name=text, group_id=id))
        return list(self.groups_cashe)

    def delete_group_by_index(self, index):
        driver = self.app.driver
        self.open_groups_page()
        self.select_group_by_index(index)
        driver.find_element_by_css_selector('input[name="delete"]').click()
        driver.find_element_by_link_text("group page").click()
        self.group_cashe = None

    def select_group_by_index(self, index):
        driver = self.app.driver
        driver.find_elements_by_css_selector('input[name="selected[]"]')[index].click()

    def modify_group_by_index(self, group, index):
        driver = self.app.driver
        self.open_groups_page()
        self.select_group_by_index(index)
        driver.find_element_by_css_selector('input[name="edit"]').click()
        self.input_group_fields(group)
        driver.find_element_by_name("update").click()
        driver.find_element_by_link_text("group page").click()
        self.group_cashe = None

    def delete_group_by_id(self, id):
        driver = self.app.driver
        self.open_groups_page()
        self.select_group_by_id(id)
        driver.find_element_by_css_selector('input[name="delete"]').click()
        driver.find_element_by_link_text("group page").click()
        self.group_cashe = None

    def select_group_by_id(self, id):
        driver = self.app.driver
        driver.find_element_by_css_selector("input[value='%s']" % id).click()
