from models.model_contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    new_cont = Contact(firstname='Stepan', middlename='Barantsev', lastname='Lol',
                                    nickname='Bloodes', email1='stepan.barantsev@gmail.com')
    app.contact.create_new_contact(new_cont)
    # Мы просто считаем группы, не выгружая полный список. Это эффективная предпроверка.
    assert len(old_contacts) + 1 == app.contact.count()   # Это типа так хеширование работает.
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(new_cont)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


