from models.model_group import Group

def test_add_group(app):
    old_groups = app.group.get_group_list()
    new_group = Group(group_name='a', group_header='b', group_footer='c')
    app.group.create_new_group(new_group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    new_group = Group(group_name='', group_header='', group_footer='')
    app.group.create_new_group(new_group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

