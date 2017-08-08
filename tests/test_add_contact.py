# -*- coding: utf-8 -*-

from models.model_contact import Contact

def test_add_contact(app):
    app.session.login('admin', 'secret')  # Вызывам тут методы объекта Application
    app.contact.create_new_contact(Contact(firstname='Stepan', middlename='Barantsev', lastname='Lol',
                                    nickname='Bloodes', email='stepan.barantsev@gmail.com'))
    app.session.logout()



