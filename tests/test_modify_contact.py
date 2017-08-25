from models.model_contact import Contact
import random


def test_modify_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new_contact(Contact(firstname='Stepan', middlename='Barantsev', lastname='Lol',
                                    nickname='Bloodes', email1='stepan.barantsev@gmail.com'))
    old_contacts = db.get_contact_list()
    new_cont = Contact(firstname='Mi', middlename='Lul', lastname='Cat',
                                    nickname='bars', email1='stepan.barantsev@gmail.com')
    cont = random.choice(old_contacts)
    new_cont.id = cont.id
    app.contact.modify_contact_by_id(new_cont, id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(cont)
    old_contacts.append(new_cont)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
