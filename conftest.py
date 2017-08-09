import pytest
from fixture.Application import Application
# Тут фикстура для всех
fixture = None
@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()        # Инициалзизация фикстуры
        fixture.session.login('admin', 'secret')
    else:
        if not fixture.is_valid():
            fixture = Application()        # Инициалзизация фикстуры
            fixture.session.login('admin', 'secret')
    return fixture

@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)  # Указание на то, как разрушить фикстуру
    return fixture