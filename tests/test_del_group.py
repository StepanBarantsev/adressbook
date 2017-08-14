from models.model_group import Group
from random import randrange


def test_del_some_group(app):
    if app.group.count() == 0:
        app.group.create_new_group(Group(group_name='a', group_header='b', group_footer='c'))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.pop(index)
    assert old_groups == new_groups



