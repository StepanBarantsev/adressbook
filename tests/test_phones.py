import re
from random import randrange


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_homepage(contact):
    return '\n'.join(filter(lambda x: x != '',
                            list(map(lambda x: clear(x),
                                     filter(lambda x: x is not None,
                                            [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone])))))


def lopata(str): # Удаляет все символы кроме цифр и букв. И все, что в скобочках тоже. Это надо для email.
    skob = False
    new_str = ''
    for i in str:
        if i == '(':
            skob = True
        if i == ')':
            skob = False
        if skob == False:
            new_str += i
    return ''.join(list(filter(None, re.split('\W', new_str))))

def to_str(contact):           # Превращает объект типа contact в строку
    if contact.homephone != '':
        contact.homephone = 'H: ' + contact.homephone
    if contact.mobilephone != '':
        contact.mobilephone = 'M: ' + contact.mobilephone
    if contact.secondaryphone != '':
        contact.secondaryphone = 'P: ' + contact.secondaryphone
    if contact.fax != '':
        contact.fax = 'F: ' + contact.fax
    if contact.homepage != '':
        contact.homepage ='Homepage: ' + contact.homepage
    if contact.workphone != '':
        contact.workphone = 'W: ' + contact.workphone
    return (contact.firstname + contact.middlename + contact.lastname +
            contact.nickname + contact.title + contact.company +
            contact.address + contact.homephone + contact.mobilephone +
            contact.workphone + contact.fax + contact.email1 + contact.email2 +
            contact.email3 + contact.homepage + contact.address + contact.secondaryphone +
            contact.notes)

def test_phones_on_homepage(app):
    index = randrange(app.contact.count())
    first_cont_from_homepage = app.contact.get_contact_list()[index]   # Можно без проблем и через индексы в цикле
    first_cont_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert first_cont_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(first_cont_from_edit_page)


def test_all_information_on_contact_view_page(app):
    index = randrange(app.contact.count())
    first_cont_from_view_page = app.contact.get_contact_from_view_page(index)
    first_cont_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    first_cont_from_edit_page = lopata(to_str(first_cont_from_edit_page))
    first_cont_from_view_page = lopata(first_cont_from_view_page.all_information)
    assert first_cont_from_view_page == first_cont_from_edit_page
