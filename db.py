# -*- coding: utf-8 -*-
from fixture.orm import ORMFixture
from models.model_group import Group


db = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')


try:
    l = db.get_contacts_not_in_group(Group(group_id=612))
    for i in l:
        print(i)
    print(len(l))
finally:
    pass
    # db.destroy()
