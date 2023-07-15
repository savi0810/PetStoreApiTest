import pytest


@pytest.fixture
def main_fixture():
    print('\nMain fixture')


@pytest.fixture()
def redefine_fixture():
    print('\n Original Redefine fixture')
