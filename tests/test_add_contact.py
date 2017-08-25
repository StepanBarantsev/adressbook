from models.model_contact import Contact


def test_add_contact(app, json_contacts, db, check_ui):
    new_cont = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create_new_contact(new_cont)
    new_contacts = db.get_contact_list()
    old_contacts.append(new_cont)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


