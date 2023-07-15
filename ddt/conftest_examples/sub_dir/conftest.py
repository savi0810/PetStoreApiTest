import pytest


@pytest.fixture()
def redefine_fixture():
    print('\n Redefined Redefine fixture')


@pytest.fixture(scope='function')
def function_fixture():
    print('\nThis fixture is called each time')


@pytest.fixture(scope='session')
def session_fixture():
    print('\nThis fixture is called once a session')


@pytest.fixture(scope='class')
def class_fixture():
    print('\nThis fixture is called once for class')


@pytest.fixture(autouse=True)#, scope='session')
def autouse_fixture():
    print('\nThis autouse')
