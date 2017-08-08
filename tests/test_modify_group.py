from models.model_group import Group

def test_modify_first_group(app):
    app.session.login(name='admin', password='secret')
    app.group.modify_first_group(Group(group_name='a', group_header='b', group_footer='c'))
    app.session.logout()