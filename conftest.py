import pytest
from fixture.Application import Application
# Тут фикстура для всех
fixture = None
@pytest.fixture
def app(request):
    global fixture
    base_url = request.config.getoption('--baseURL')
    browser = request.config.getoption('--browser')
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url)        # Инициалзизация фикстуры
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_url=base_url)        # Инициалзизация фикстуры
    fixture.session.ensure_login('admin', 'secret')
    return fixture

@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)  # Указание на то, как разрушить фикстуру
    return fixture


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')
    parser.addoption('--baseURL', action='store', default='http://localhost/addressbook/')