import pymysql.cursors
from models.model_group import Group
from models.model_contact import Contact

class DbFixture:

    def __init__(self, name, user, password, host):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, charset='utf8', autocommit=True)
        self.connection.autocommit = True   # Чтобы не ,было кеширования

    def destroy(self):
        self.connection.close()


    def get_group_list(self):
        cursor = self.connection.cursor()
        s = []
        try:
            cursor.execute('select group_id, group_name, group_header, group_footer from group_list')
            for row in cursor:
                id, name, header, footer = row
                s.append(Group(group_id=str(id), group_header=header, group_name=name, group_footer=footer))
        finally:
            cursor.close()
        return s


    def get_contact_list(self):
        cursor = self.connection.cursor()
        s = []
        try:
            cursor.execute("select id, firstname, middlename, lastname, nickname, company, title, address, "
                           "home, mobile, work, fax, email, email2, email3, homepage, "
                           "notes, phone2  from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                id, firstname, middlename,  lastname, nickname, company, title, address,\
                homephone, mobilephone, workphone, fax, email, email2, email3, homepage, notes, secondaryphone = row

                s.append(Contact(firstname=firstname, lastname=lastname, id=str(id), homephone=homephone,
                       mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone,
                       email1=email, email2=email2, email3=email3, address=address, middlename=middlename,
                       nickname=nickname, title=title, company=company, homepage=homepage, notes=notes, fax=fax))
        finally:
            cursor.close()
        return s

