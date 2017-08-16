from random import randrange
from tests.test_phones import merge_phones_like_on_homepage


def merge_emails_like_on_homepage(contact):
    return '\n'.join(filter(lambda x: x != '',
                       filter(lambda x: x is not None,
                         [contact.email1, contact.email2, contact.email3])))


def test_eq_of_random_contact(app):   # Это сравнение с edit и homepage всех полей
    index = randrange(app.contact.count())
    first_cont_from_homepage = app.contact.get_contact_list()[index]
    first_cont_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert first_cont_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(first_cont_from_edit_page)
    assert first_cont_from_homepage.allemails == merge_emails_like_on_homepage(first_cont_from_edit_page)
    assert first_cont_from_homepage.firstname == first_cont_from_edit_page.firstname
    assert first_cont_from_homepage.lastname == first_cont_from_edit_page.lastname
    assert first_cont_from_homepage.address == first_cont_from_edit_page.address