import pytest
from fixture.Application import Application
# Тут фикстура для всех
@pytest.fixture(scope='session') # scope='session' Чтобы 1 раз браузер открылся
def app(request):
    fixture = Application()        # Инициалзизация фикстуры
    request.addfinalizer(fixture.destroy)  # Указание на то, как разрушить фикстуру
    return fixture