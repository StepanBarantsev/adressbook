from pony.orm import *
from datetime import datetime
from models.model_group import Group
from models.model_contact import Contact
from pymysql.converters import decoders

class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact, table='address_in_groups', column='id', reverse='groups', lazy=True)

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        middlename = Optional(str, column='middlename')
        lastname = Optional(str, column='lastname')
        nickname = Optional(str, column='nickname')
        company = Optional(str, column='company')
        title = Optional(str, column='title')
        address = Optional(str, column='address')
        homephone = Optional(str, column='home')
        mobilephone = Optional(str, column='mobile')
        workphone = Optional(str, column='work')
        fax = Optional(str, column='fax')
        email1 = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        homepage = Optional(str, column='homepage')
        notes = Optional(str, column='notes')
        secondaryphone = Optional(str, column='phone2')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table='address_in_groups', column='group_id', reverse='contacts', lazy=True)

    def __init__(self, name, user, password, host):
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=decoders)
        self.db.generate_mapping()

    def convert_groups_to_models(self, groups):
        def convert(group):
            return Group(group_id=str(group.id), group_name=group.name, group_header=group.header, group_footer=group.footer)
        return list(map(convert, groups))

    def convert_contacts_to_models(self, contacts):
        def convert(contact):
            return Contact(firstname=contact.firstname, lastname=contact.lastname, id=contact.id, homephone=contact.homephone,
                       mobilephone=contact.mobilephone, workphone=contact.workphone, secondaryphone=contact.secondaryphone,
                       email1=contact.email1, email2=contact.email2, email3=contact.email3, address=contact.address,
                       middlename=contact.middlename,
                       nickname=contact.nickname, title=contact.title, company=contact.company,
                       homepage=contact.homepage, notes=contact.notes, fax=contact.fax)
        return list(map(convert, contacts))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_models(select(g for g in ORMFixture.ORMGroup))


    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_models(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.group_id))[0]
        return self.convert_contacts_to_models(orm_group.contacts)


    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.group_id))[0]
        return self.convert_contacts_to_models(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))


