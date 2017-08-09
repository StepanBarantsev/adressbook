from models.model_contact import Contact

def test_add_contact(app):
    app.contact.create_new_contact(Contact(firstname='Stepan', middlename='Barantsev', lastname='Lol',
                                    nickname='Bloodes', email='stepan.barantsev@gmail.com'))
    app.session.logout()



