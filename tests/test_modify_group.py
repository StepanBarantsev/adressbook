from models.model_group import Group

def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create_new_group(Group(group_name='a', group_header='b', group_footer='c'))
    app.group.modify_first_group(Group(group_name='a', group_header='b', group_footer='c'))
