from models.model_group import Group

def test_add_group(app):
    app.group.create_new_group(Group(group_name='a', group_header='b', group_footer='c'))


def test_add_empty_group(app):
    app.group.create_new_group(Group(group_name='', group_header='', group_footer=''))


