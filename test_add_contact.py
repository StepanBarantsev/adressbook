# -*- coding: utf-8 -*-
from model_contact import Contact
from Application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()        # Инициалзизация фикстуры
    request.addfinalizer(fixture.destroy)  # Указание на то, как разрушить фикстуру
    return fixture

def test_add_contact(app):
    app.login('admin', 'secret')
    app.create_new_contact(Contact(firstname='Stepan', middlename='Barantsev', lastname='Lol',
                                    nickname='Bloodes', email='stepan.barantsev@gmail.com'))
    app.logout()



