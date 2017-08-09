import pytest
from fixture.Application import Application
# Тут фикстура для всех
@pytest.fixture(scope='session') # scope='session' Чтобы 1 раз браузер открылся
def app(request):
    fixture = Application()        # Инициалзизация фикстуры
    fixture.session.login('admin', 'secret')
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)  # Указание на то, как разрушить фикстуру
    return fixture