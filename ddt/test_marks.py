import pytest


@pytest.mark.scope1
@pytest.mark.regress
def test_scope1():
    print('\nTest scope1')


@pytest.mark.scope2
@pytest.mark.regress
def test_scope2():
    print('\nTest scope2')
