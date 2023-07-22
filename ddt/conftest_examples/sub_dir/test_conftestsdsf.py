import pytest


def test_call_main_fixture(main_fixture):
    print('\n test call main fixture')


def test_call_redefine_fixture(redefine_fixture):
    print('\n test call redefine fixture')


@pytest.mark.parametrize('input_value', [1, 2, 3])
def test_with_scope(session_fixture, function_fixture, input_value):
    print(f'\n Test input: {input_value}')


class TestClass:
    @pytest.mark.parametrize('input_value', [1, 2, 3])
    def test_with_scope_class(self, session_fixture, class_fixture, function_fixture, input_value):
        print(f'\n Test input: {input_value}')

    @pytest.mark.parametrize('input_value', [4, 5, 6])
    def test_with_scope_class_2(self, session_fixture, class_fixture, function_fixture, input_value):
        print(f'\n Test input: {input_value}')
