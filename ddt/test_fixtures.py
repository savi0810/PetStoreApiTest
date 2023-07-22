import pytest


@pytest.fixture
def fixture_1():
    print('\nFixture 1: Enter\n')


def test_with_fixture_1(fixture_1):
    print('Test with fixture 1\n')
##########


@pytest.fixture
def fixture_yield():
    print('\nFixture yield: Enter\n')
    yield
    print('\nFixture yield: Exit\n')


def test_with_fixture_yield(fixture_yield):
    print('Test with fixture yield\n')
##########


@pytest.fixture
def fixture_nested_first():
    print('\nFixture nested_first: Enter\n')
    yield '4'
    print('\nFixture nested_first: Exit\n')


@pytest.fixture
def fixture_nested_second(fixture_nested_first):
    t = fixture_nested_first
    print('\nFixture nested_second: Enter\n')
    yield
    print('\nFixture nested_second: Exit\n')


def test_with_fixture_nested(fixture_nested_second):
    print('Test with fixture nested\n')
##########


@pytest.fixture
def fixture_return():
    print('\nFixture return: Enter\n')
    # return 'fixture value'
    # return 12345
    # return [1, 2, 3, 4]
    return {'name': 'Tom', 'lastname': 'Tomson'}


def test_with_fixture_return(fixture_return):
    print(f'Test got fixture value "{fixture_return}" \n')
##########


@pytest.fixture
def fixture_yield_value():
    print('\nFixture yield value: Enter\n')
    yield {'name': 'Tom', 'lastname': 'Tomson'}
    print('\nFixture yield value: Exit\n')


def test_with_fixture_yield_value(fixture_yield_value):
    print(f'Test got fixture value "{fixture_yield_value}" \n')
##########


@pytest.fixture(params=[1, 2, 3, 4])
def fixture_params_list(request):
    print(f'\nFixture param: {request.param}\n')
    return request.param


def test_with_fixture_params_list(fixture_params_list):
    print(f'Test got fixture value "{fixture_params_list}" \n')

##########


@pytest.fixture(params=[1, 2, 3, 4], ids=['one', 'two', 'three', 'four'])
def fixture_params_ids(request):
    print(f'\nFixture param: {request.param}\n')
    return request.param


def test_with_fixture_params_ids(fixture_params_ids):
    print(f'Test got fixture value "{fixture_params_list}" \n')
##########


@pytest.fixture(params=[
    (1, 2),
    (3, 4),
    (5, 6),
])
def fixture_list(request):
    print(f'\nFixture param: {request.param}\n')
    return request.param


def test_with_fixture_list(fixture_list):
    print(f'Test got fixture value "{fixture_list}" \n')
    # p1, p2 = fixture_list
    # print(f'Test got fixture value p1 "{p1}", p2 "{p2}" \n')
##########


@pytest.fixture(params=[
    pytest.param((1, 2), id='first'),
    pytest.param((3, 4), id='second'),
    pytest.param((5, 6), id='third', marks=pytest.mark.skip('BUG-345')),
])
def fixture_param(request):
    print(f'\nFixture param: {request.param}\n')
    return request.param


def test_with_fixture_param(fixture_param):
    print(f'Test got fixture value "{fixture_param}" \n')
##########


@pytest.mark.parametrize("expected", [3, 11])
def test_with_params(fixture_param, expected):
    p1, p2 = fixture_param
    assert p1 + p2 == expected
##########


@pytest.fixture(params=[1, 2, 3, 4])
def fixture_params_nested_first(request):
    return request.param


@pytest.fixture(params=[10, 20, 30, 40])
def fixture_params_nested_second(request, fixture_params_nested_first):
    return request.param + fixture_params_nested_first


# @pytest.mark.parametrize('add', [100, 200, 300, 400])
def test_with_fixture_params_nested(fixture_params_nested_second):
    print(f'Test got fixture value "{fixture_params_nested_second}" \n')



