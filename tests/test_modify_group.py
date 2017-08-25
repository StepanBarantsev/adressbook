from models.model_group import Group
import random


def test_modify_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create_new_group(Group(group_name='a', group_header='b', group_footer='c'))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group = Group(group_name='k', group_header='b', group_footer='y')
    new_group.group_id = group.group_id
    app.group.modify_group_by_id(new_group, group.group_id)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

