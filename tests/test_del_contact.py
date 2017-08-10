from models.model_contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(firstname='Stepan', middlename='Barantsev', lastname='Lol',
                                    nickname='Bloodes', email='stepan.barantsev@gmail.com'))
    app.contact.delete_first_contact()

