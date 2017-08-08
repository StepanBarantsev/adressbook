# -*- coding: utf-8 -*-
import pytest

from fixture.Application import Application
from models.model_contact import Contact


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



