from models.model_group import Group
from random import randrange


def test_modify_some_group(app):
    if app.group.count() == 0:
        app.group.create_new_group(Group(group_name='a', group_header='b', group_footer='c'))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    new_group = Group(group_name='k', group_header='b', group_footer='y')
    new_group.group_id = old_groups[index].group_id
    app.group.modify_group_by_index(new_group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = new_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

