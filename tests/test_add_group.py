# -*- coding: utf-8 -*-

from models.model_group import Group

def test_add_group(app):
    app.session.login(name='admin', password='secret')    # Вызывам тут методы объекта Application
    app.group.create_new_group(Group(group_name='a', group_header='b', group_footer='c'))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(name='admin', password='secret')
    app.group.create_new_group(Group(group_name='', group_header='', group_footer=''))
    app.session.logout()

