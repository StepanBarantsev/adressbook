import re

def clear(s):             # clear пока не работает, хз почему
    re.sub("[- ]", '', s)


def test_phones_on_homepage(app):
    first_cont_from_homepage = app.contact.get_contact_list()[0]
    first_cont_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert first_cont_from_homepage.homephone == first_cont_from_edit_page.homephone
    assert first_cont_from_homepage.mobilephone == first_cont_from_edit_page.mobilephone
    assert first_cont_from_homepage.workphone == first_cont_from_edit_page.workphone
    assert first_cont_from_homepage.secondaryphone == first_cont_from_edit_page.secondaryphone

def test_phones_on_contact_view_page(app):
    first_cont_from_view_page = app.contact.get_contact_from_view_page(0)
    first_cont_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert first_cont_from_view_page.homephone == first_cont_from_edit_page.homephone
    assert first_cont_from_view_page.mobilephone == first_cont_from_edit_page.mobilephone
    assert first_cont_from_view_page.workphone == first_cont_from_edit_page.workphone
    assert first_cont_from_view_page.secondaryphone == first_cont_from_edit_page.secondaryphone