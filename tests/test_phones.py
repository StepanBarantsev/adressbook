import re


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_homepage(contact):
    return '\n'.join(filter(lambda x: x != '',
                            list(map(lambda x: clear(x),
                                     filter(lambda x: x is not None,
                                            [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone])))))


def test_phones_on_homepage(app):
    first_cont_from_homepage = app.contact.get_contact_list()[0]   # Можно без проблем и через индексы в цикле
    first_cont_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert first_cont_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(first_cont_from_edit_page)


#def test_phones_on_contact_view_page(app):
#    first_cont_from_view_page = app.contact.get_contact_from_view_page(0)
#    first_cont_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#    assert first_cont_from_view_page.homephone == first_cont_from_edit_page.homephone
#    assert first_cont_from_view_page.mobilephone == first_cont_from_edit_page.mobilephone
#   assert first_cont_from_view_page.workphone == first_cont_from_edit_page.workphone
#   assert first_cont_from_view_page.secondaryphone == first_cont_from_edit_page.secondaryphone