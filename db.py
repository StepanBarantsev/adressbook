# -*- coding: utf-8 -*-
from fixture.db import DbFixture


db = DbFixture(host='127.0.0.1', name='addressbook', user='root', password='')


try:
    contacts = db.get_contact_list()
    for con in contacts:
        print(con)
    print(len(contacts))
finally:
    db.destroy()