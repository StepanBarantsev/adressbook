from models.model_group import Group

def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create_new_group(Group(group_name='a', group_header='b', group_footer='c'))
    old_groups = app.group.get_group_list()
    new_group = Group(group_name='k', group_header='b', group_footer='y')
    new_group.group_id = old_groups[0].group_id
    app.group.modify_first_group(new_group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = new_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

