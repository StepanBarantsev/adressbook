from models.model_contact import Contact
from random import randrange


def test_modify_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(firstname='Stepan', middlename='Barantsev', lastname='Lol',
                                    nickname='Bloodes', email1='stepan.barantsev@gmail.com'))
    old_contacts = app.contact.get_contact_list()
    new_cont = Contact(firstname='Mi', middlename='Lul', lastname='Cat',
                                    nickname='bars', email1='stepan.barantsev@gmail.com')
    index = randrange(len(old_contacts))
    new_cont.id = old_contacts[index].id
    app.contact.modify_contact_by_index(new_cont, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = new_cont
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
