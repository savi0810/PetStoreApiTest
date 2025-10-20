import requests
import pytest

BASE_URL_PETSTORE = 'https://petstore.swagger.io/v2'


class TestStore:
    
    @pytest.fixture
    def order_data(self):
        return {
            'id': 1521,
            'petId': 1,
            'quantity': 1,
            'shipDate': '2023-10-01T10:00:00.000Z',
            'status': 'placed',
            'complete': True
        }
    
    @pytest.fixture
    def created_order(self, order_data):
        response = requests.post(f'{BASE_URL_PETSTORE}/store/order', json=order_data)
        assert response.status_code == 200
        yield order_data
        requests.delete(f'{BASE_URL_PETSTORE}/store/order/{order_data["id"]}')

    def test_get_store_inventory(self):
        response = requests.get(f'{BASE_URL_PETSTORE}/store/inventory')
        assert response.status_code == 200
        assert response.reason == 'OK'
        inventory = response.json()
        assert isinstance(inventory, dict)
        expected_statuses = ['available', 'pending', 'sold']
        for status in expected_statuses:
            assert status in inventory

    def test_create_order(self, order_data):
        response = requests.post(f'{BASE_URL_PETSTORE}/store/order', json=order_data)
        assert response.status_code == 200
        assert response.reason == 'OK'
        order_response = response.json()
        assert order_response['id'] == order_data['id']
        assert order_response['petId'] == order_data['petId']
        assert order_response['quantity'] == order_data['quantity']
        assert order_response['status'] == order_data['status']
        assert order_response['complete'] == order_data['complete']
        requests.delete(f'{BASE_URL_PETSTORE}/store/order/{order_data["id"]}')

    def test_get_order_after_creation(self, created_order):
        response = requests.get(f'{BASE_URL_PETSTORE}/store/order/{created_order["id"]}')
        assert response.status_code == 200
        assert response.reason == 'OK'
        order_info = response.json()
        assert order_info['id'] == created_order['id']
        assert order_info['petId'] == created_order['petId']
        assert order_info['quantity'] == created_order['quantity']
        assert order_info['status'] == created_order['status']
        assert order_info['complete'] == created_order['complete']

    def test_delete_order(self, created_order):
        response = requests.delete(f'{BASE_URL_PETSTORE}/store/order/{created_order["id"]}')
        assert response.status_code == 200
        assert response.reason == 'OK'
        response_data = response.json()
        assert response_data['code'] == 200
        assert response_data['type'] == 'unknown'
        response = requests.get(f'{BASE_URL_PETSTORE}/store/order/{created_order["id"]}')
        assert response.status_code == 404

    @pytest.mark.parametrize("order_data", [
        {
            'id': 1522,
            'petId': 2,
            'quantity': 3,
            'shipDate': '2023-10-01T10:00:00.000Z',
            'status': 'approved',
            'complete': False
        },
        {
            'id': 1523,
            'petId': 3,
            'quantity': 5,
            'shipDate': '2023-10-01T10:00:00.000Z',
            'status': 'delivered',
            'complete': True
        }
    ])
    def test_create_different_orders(self, order_data):
        response = requests.post(f'{BASE_URL_PETSTORE}/store/order', json=order_data)
        assert response.status_code == 200
        order_response = response.json()
        assert order_response['id'] == order_data['id']
        assert order_response['petId'] == order_data['petId']
        assert order_response['quantity'] == order_data['quantity']
        assert order_response['status'] == order_data['status']
        requests.delete(f'{BASE_URL_PETSTORE}/store/order/{order_data["id"]}')

    @pytest.mark.parametrize("invalid_order_id,expected_code", [
        (-1, 404),
        (0, 404),
        (999999, 404)
    ])
    def test_get_invalid_orders(self, invalid_order_id, expected_code):
        response = requests.get(f'{BASE_URL_PETSTORE}/store/order/{invalid_order_id}')
        assert response.status_code == expected_code