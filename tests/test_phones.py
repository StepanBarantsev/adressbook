import re
from random import randrange


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_homepage(contact):
    return '\n'.join(filter(lambda x: x != '',
                            list(map(lambda x: clear(x),
                                     filter(lambda x: x is not None,
                                            [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone])))))


def test_phones_on_homepage(app):
    index = randrange(app.contact.count())
    first_cont_from_homepage = app.contact.get_contact_list()[index]   # Можно без проблем и через индексы в цикле
    first_cont_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert first_cont_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(first_cont_from_edit_page)


#def test_phones_on_contact_view_page(app):
#    index = randrange(app.contact.count())
#    first_cont_from_view_page = app.contact.get_contact_from_view_page(index)
#    first_cont_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#    assert merge_all_like_on_view_page(first_cont_from_edit_page) == first_cont_from_view_page.all_informaion # Тут нет метода, ну да и я хз что делать
