import requests
import pprint
import json

BASE_URL_PETSTORE = 'https://petstore.swagger.io/v2'

print("=== TESTS FOR USER ===")

print("\n1. GET User (before creation):")
response = requests.get(f'{BASE_URL_PETSTORE}/user/testuser1135')

pprint.pprint(response.url)
pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.text)
if response.text:
    pprint.pprint(response.json())
pprint.pprint('**********')

print("\n2. POST User - Create:")
user_data = {
    'id': 1135,
    'username': 'testuser1135',
    'firstName': 'Test',
    'lastName': 'User',
    'email': 'test@example.com',
    'password': 'testpass',
    'phone': '123456789',
    'userStatus': 135
}
response = requests.post(f'{BASE_URL_PETSTORE}/user', json=user_data)

pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.text)


print("\n3. GET User after creation:")
response = requests.get(f'{BASE_URL_PETSTORE}/user/testuser1135')
pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.text)

if response.text:
    user_info = json.loads(response.text)
    pprint.pprint(user_info)
    
pprint.pprint('**********')

print("\n4. DELETE User:")
response = requests.delete(f'{BASE_URL_PETSTORE}/user/testuser1135')

pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.text)
pprint.pprint('**********')

print("\n5. GET User after deletion:")
response = requests.get(f'{BASE_URL_PETSTORE}/user/testuser1135')

pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.text)
if response.text:
    pprint.pprint(response.json())
    
pprint.pprint('**********')

print("\n=== TESTS FOR STORE ===")

print("\n1. GET Store Inventory:")
response = requests.get(f'{BASE_URL_PETSTORE}/store/inventory')

pprint.pprint(response.url)
pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.text)
if response.text:
    inventory_data = response.json()
    pprint.pprint(inventory_data)

pprint.pprint('**********')

print("\n2. POST Store Order:")
order_id = 1521

order_data = {
    'id': order_id,
    'petId': 1,
    'quantity': 1,
    'shipDate': '2023-10-01T10:00:00.000Z',
    'status': 'placed',
    'complete': True
}
response = requests.post(f'{BASE_URL_PETSTORE}/store/order', json=order_data)

pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.text)

if response.text:
    order_response = json.loads(response.text)
    pprint.pprint(order_response)    
    
print("\n3. GET Store Order after creation:")
response = requests.get(f'{BASE_URL_PETSTORE}/store/order/{order_id}')

pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.text)

if response.text:
    order_info = json.loads(response.text)
    pprint.pprint(order_info)
            
pprint.pprint('**********')

print("\n4. DELETE Store Order:")
response = requests.delete(f'{BASE_URL_PETSTORE}/store/order/{order_id}')

pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.text)
    
pprint.pprint('**********')

print("\n5. GET Store Order after deletion:")
response = requests.get(f'{BASE_URL_PETSTORE}/store/order/{order_id}')

pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.text)
if response.text:
    pprint.pprint(response.json())
        
pprint.pprint('**********')