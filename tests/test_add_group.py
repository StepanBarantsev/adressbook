# -*- coding: utf-8 -*-
import pytest

from fixture.Application import Application
from models.model_group import Group


@pytest.fixture
def app(request):
    fixture = Application()        # Инициалзизация фикстуры
    request.addfinalizer(fixture.destroy)  # Указание на то, как разрушить фикстуру
    return fixture

def test_add_group(app):
    app.login(name='admin', password='secret')    # Вызывам тут методы объекта Application
    app.create_new_group(Group(group_name='a', group_header='b', group_footer='c'))
    app.logout()

def test_add_empty_group(app):
    app.login(name='admin', password='secret')
    app.create_new_group(Group(group_name='', group_header='', group_footer=''))
    app.logout()

