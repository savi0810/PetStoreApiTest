import requests
import pytest

BASE_URL_PETSTORE = 'https://petstore.swagger.io/v2'


class TestUser:
    
    @pytest.fixture
    def user_data(self):
        return {
            'id': 1135,
            'username': 'testuser1135',
            'firstName': 'Test',
            'lastName': 'User',
            'email': 'test@example.com',
            'password': 'testpass',
            'phone': '123456789',
            'userStatus': 135
        }
    
    @pytest.fixture
    def created_user(self, user_data):
        response = requests.post(f'{BASE_URL_PETSTORE}/user', json=user_data)
        assert response.status_code == 200
        yield user_data
        requests.delete(f'{BASE_URL_PETSTORE}/user/{user_data["username"]}')

    def test_get_nonexistent_user(self):
        response = requests.get(f'{BASE_URL_PETSTORE}/user/testuser1135')
        assert response.status_code == 404
        assert response.reason == 'Not Found'
        response_data = response.json()
        assert response_data['code'] == 1
        assert response_data['type'] == 'error'

    def test_create_user(self, user_data):
        response = requests.post(f'{BASE_URL_PETSTORE}/user', json=user_data)
        assert response.status_code == 200
        assert response.reason == 'OK'
        response_data = response.json()
        assert response_data['code'] == 200
        assert response_data['type'] == 'unknown'
        requests.delete(f'{BASE_URL_PETSTORE}/user/{user_data["username"]}')

    def test_get_user_after_creation(self, created_user):
        response = requests.get(f'{BASE_URL_PETSTORE}/user/{created_user["username"]}')
        assert response.status_code == 200
        assert response.reason == 'OK'
        user_info = response.json()
        assert user_info['id'] == created_user['id']
        assert user_info['username'] == created_user['username']
        assert user_info['email'] == created_user['email']
        assert user_info['firstName'] == created_user['firstName']
        assert user_info['lastName'] == created_user['lastName']

    def test_delete_user(self, created_user):
        response = requests.delete(f'{BASE_URL_PETSTORE}/user/{created_user["username"]}')
        assert response.status_code == 200
        assert response.reason == 'OK'
        response_data = response.json()
        assert response_data['code'] == 200
        assert response_data['type'] == 'unknown'
        response = requests.get(f'{BASE_URL_PETSTORE}/user/{created_user["username"]}')
        assert response.status_code == 404

    @pytest.mark.parametrize("user_data", [
        {
            'id': 1136,
            'username': 'testuser1136',
            'firstName': 'Alexn',
            'lastName': 'e',
            'email': 'alex@example.com',
            'password': 'password123',
            'phone': '111111111',
            'userStatus': 1
        },
        {
            'id': 1137,
            'username': 'testuser1137',
            'firstName': 'Jane',
            'lastName': 'S',
            'email': 'jane@example.com',
            'password': 'password456',
            'phone': '222222222',
            'userStatus': 2
        }
    ])
    def test_create_different_users(self, user_data):
        response = requests.post(f'{BASE_URL_PETSTORE}/user', json=user_data)
        assert response.status_code == 200
        response_data = response.json()
        assert response_data['code'] == 200
        requests.delete(f'{BASE_URL_PETSTORE}/user/{user_data["username"]}')
        
    @pytest.mark.parametrize("invalid_username,expected_code", [
        ("dddd", 404),
        ("ggg", 404),
        ("Vasya", 404)
    ])
    def test_get_invalid_users(self, invalid_username, expected_code):
        response = requests.get(f'{BASE_URL_PETSTORE}/user/{invalid_username}')
        assert response.status_code == expected_code