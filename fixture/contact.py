from models.model_contact import Contact
import re
from selenium.webdriver.support.ui import Select

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
        if contact.email1 != None:
            driver.find_element_by_name("email").clear()
            driver.find_element_by_name("email").send_keys(contact.email1)
        if contact.homephone != None:
            driver.find_element_by_name("home").clear()
            driver.find_element_by_name("home").send_keys(contact.homephone )
        if contact.mobilephone != None:
            driver.find_element_by_name('mobile').clear()
            driver.find_element_by_name('mobile').send_keys(contact.mobilephone)
        if contact.workphone != None:
            driver.find_element_by_name('work').clear()
            driver.find_element_by_name('work').send_keys(contact.workphone)
        if contact.secondaryphone != None:
            driver.find_element_by_name('phone2').clear()
            driver.find_element_by_name('phone2').send_keys(contact.secondaryphone)
        if contact.address != None:
            driver.find_element_by_name("address").clear()
            driver.find_element_by_name("address").send_keys(contact.address)
        if contact.email2 != None:
            driver.find_element_by_name("email2").clear()
            driver.find_element_by_name("email2").send_keys(contact.email2)
        if contact.email3 != None:
            driver.find_element_by_name("email3").clear()
            driver.find_element_by_name("email3").send_keys(contact.email3)
        if contact.title != None:
            driver.find_element_by_name('title').clear()
            driver.find_element_by_name('title').send_keys(contact.title)
        if contact.notes != None:
            driver.find_element_by_name('notes').clear()
            driver.find_element_by_name('notes').send_keys(contact.notes)
        if contact.company != None:
            driver.find_element_by_name('company').clear()
            driver.find_element_by_name('company').send_keys(contact.company)
        if contact.homepage != None:
            driver.find_element_by_name('homepage').clear()
            driver.find_element_by_name('homepage').send_keys(contact.homepage)
        if contact.fax != None:
            driver.find_element_by_name('fax').clear()
            driver.find_element_by_name('fax').send_keys(contact.fax)

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
            for row in driver.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = row.find_element_by_css_selector('input[name="selected[]"]').get_attribute('value')
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                allemails = cells[4].text
                all_phones = cells[5].text
                self.cont_cashe.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                               all_phones_from_homepage=all_phones, address=address,
                                               allemails=allemails))
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
        self.open_contact_to_edit_by_index(index)
        self.input_contact_fields(contact)
        driver.find_element_by_css_selector('input[name="update"]').click()
        driver.find_element_by_link_text("home page").click()
        self.cont_cashe = None

    def open_contact_to_edit_by_index(self, index):
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_elements_by_css_selector('img[alt="Edit"]')[index].click()

    def open_contact_view_by_index(self, index):
        driver = self.app.driver
        self.app.open_home_page()
        row = driver.find_elements_by_css_selector('tr[name="entry"]')[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_css_selector('img[title="Details"]').click()

    def get_contact_info_from_edit_page(self, index):
        driver = self.app.driver
        self.app.open_home_page()
        self.open_contact_to_edit_by_index(index)
        firstname = driver.find_element_by_name('firstname').get_attribute('value')
        lastname = driver.find_element_by_name('lastname').get_attribute('value')
        address = driver.find_element_by_name("address").get_attribute("value")
        id = driver.find_element_by_name('id').get_attribute('value')
        email = driver.find_element_by_name("email").get_attribute("value")
        email2 = driver.find_element_by_name("email2").get_attribute("value")
        email3 = driver.find_element_by_name("email3").get_attribute("value")
        homephone = driver.find_element_by_name('home').get_attribute('value')
        mobilephone = driver.find_element_by_name('mobile').get_attribute('value')
        workphone = driver.find_element_by_name('work').get_attribute('value')
        secondaryphone = driver.find_element_by_name('phone2').get_attribute('value')
        middlename = driver.find_element_by_name('middlename').get_attribute('value')
        nickname = driver.find_element_by_name('nickname').get_attribute('value')
        title = driver.find_element_by_name('title').get_attribute('value')
        company = driver.find_element_by_name('company').get_attribute('value')
        homepage = driver.find_element_by_name('homepage').get_attribute('value')
        notes = driver.find_element_by_name('notes').get_attribute('value')
        fax = driver.find_element_by_name('fax').get_attribute('value')
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone,
                       mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone,
                       email1=email, email2=email2, email3=email3, address=address, middlename=middlename,
                       nickname=nickname, title=title, company=company, homepage=homepage, notes=notes, fax=fax)

    def get_contact_from_view_page(self, index):
        driver = self.app.driver
        self.open_contact_view_by_index(index)
        all_inf = driver.find_element_by_css_selector('div#content').text      # Тут все данные считываются лопатой
        return Contact(all_information=all_inf)

    def delete_contact_by_id(self, id):
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_element_by_css_selector("input[value='%s']" % id).click()
        driver.find_element_by_css_selector("input[value='Delete']").click()
        driver.switch_to_alert().accept()
        driver.find_element_by_link_text("home").click()
        self.cont_cashe = None

    def modify_contact_by_id(self, contact, id):
        driver = self.app.driver
        self.app.open_home_page()
        self.open_contact_to_edit_by_id(id)
        self.input_contact_fields(contact)
        driver.find_element_by_css_selector('input[name="update"]').click()
        driver.find_element_by_link_text("home page").click()
        self.cont_cashe = None

    def open_contact_to_edit_by_id(self, id):
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_element_by_css_selector('a[href="edit.php?id=%s"]' % id).click()

    def add_contact_to_group(self, contact, group):
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_element_by_css_selector("input[value='%s']" % contact.id).click()
        driver.find_element_by_name("to_group").find_element_by_css_selector("option[value='%s']" % group.group_id).click()
        driver.find_element_by_name("add").click()


