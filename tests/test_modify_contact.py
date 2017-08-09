from models.model_contact import Contact


def test_modify_first_contact(app):
    app.contact.modify_first_contact(Contact(firstname='Stepan', middlename='Barantsev', lastname='Lol',
                                    nickname='Bloodes', email='stepan.barantsev@gmail.com'))
