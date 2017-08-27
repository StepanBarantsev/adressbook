from models.model_contact import Contact
from models.model_group import Group
import random


def test_add_contact_to_group(app, db, check_ui):
    contact_list = db.get_contact_list()
    if len(contact_list) == 0:
        app.contact.create_new_contact(Contact(firstname="FF", lastname="HH", nickname="bbb"))
        contact_list = db.get_contact_list()
    group_list = db.get_group_list()
    if len(group_list) == 0:
        app.group.create_new_group(Group(group_name="New group", group_header='Zez', group_footer='Freytr'))
        group_list = db.get_group_list()
    contact = random.choice(contact_list)
    group = random.choice(group_list)
    contacts_in_group = db.get_contacts_in_group(group)
    app.contact.add_contact_to_group(contact, group)
    new_contacts_in_group = db.get_contacts_in_group(group)
    contacts_in_group.append(contact)
    assert sorted(contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts_in_group, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)