from models.model_contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return  prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname='Stepan', middlename='Barantsev', lastname='Lol',
                                    nickname='Bloodes', email1='stepan.barantsev@gmail.com')] +\
           [Contact(firstname=random_string('', 10),
                    middlename=random_string('', 20),
                    lastname=random_string('', 20),
                    nickname=random_string('', 20),
                    homephone=random_string('', 20),
                    mobilephone=random_string('', 20),
                    workphone=random_string('', 20),
                    secondaryphone=random_string('', 20),
                    email1=random_string('', 20),
                    email2=random_string('', 20),
                    email3=random_string('', 20),
                    title=random_string('', 20),
                    notes=random_string('', 20),
                    company=random_string('', 20),
                    homepage=random_string('', 20),
                    fax=random_string('', 20))
            for i in range(5)
            ]
@pytest.mark.parametrize('new_cont', testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, new_cont):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_new_contact(new_cont)
    # Мы просто считаем группы, не выгружая полный список. Это эффективная предпроверка.
    assert len(old_contacts) + 1 == app.contact.count()   # Это типа так хеширование работает.
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(new_cont)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


