from models.model_contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(firstname='Stepan', middlename='Barantsev', lastname='Lol',
                                    nickname='Bloodes', email='stepan.barantsev@gmail.com'))
    old_contacts = app.contact.get_contact_list()
    new_cont = Contact(firstname='Stepan', middlename='Barantsev', lastname='Lol',
                                    nickname='Bloodes', email='stepan.barantsev@gmail.com')
    new_cont.id = old_contacts[0].id
    app.contact.modify_first_contact(new_cont)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = new_cont
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
