from models.model_contact import Contact
from models.model_group import Group
import random


def test_delete_contact_from_group(app, db):

    contact_list = db.get_contact_list()
    if len(contact_list) == 0:
        app.contact.create_new_contact(Contact(firstname="FF", lastname="HH", nickname="bbb"))
        contact_list = db.get_contact_list()
    group_list = db.get_group_list()
    if len(group_list) == 0:
        app.group.create_new_group(Group(group_name="New group", group_header='Zez', group_footer='Freytr'))
        group_list = db.get_group_list()

    all_groups = list(gr for gr in db.get_group_list() if len(db.get_contacts_in_group(gr)))

    if not all_groups:
        contact = random.choice(contact_list)
        group = random.choice(group_list)
        app.contact.add_contact_to_group(contact, group)
        all_groups = list(gr for gr in db.get_group_list() if len(db.get_contacts_in_group(gr)))

    group = random.choice(all_groups)
    all_contacts = db.get_contacts_in_group(group)
    contact = random.choice(all_contacts)
    app.contact.delete_contact_from_group(contact, group)
    all_contacts.remove(contact)
    all_new_contacts = db.get_contacts_in_group(group)
    assert sorted(all_new_contacts, key=Contact.id_or_max) == sorted(all_contacts, key=Contact.id_or_max)
    assert contact not in db.get_contacts_in_group(group)
    assert contact in db.get_contacts_not_in_group(group)