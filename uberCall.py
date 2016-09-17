from uber_rides.session import Session
session = Session(server_token='60KIlvmpVK8JWNiNvau69NTqziJsT-0KM9e0Hlfb')
from uber_rides.client import UberRidesClient
client = UberRidesClient(session)
response = client.get_products(37.77, -122.41)
products = response.json.get('products')

print('~~~~~~~~~~~~~')
print(products)
print('~~~~~~~~~~~~~')
client = UberRidesClient(session, sandbox_mode=True)
response = client.request_ride(
    product_id=products[0].get('product_id'),
    start_latitude=37.77,
    start_longitude=-122.41,
    end_latitude=37.79,
    end_longitude=-122.35,
)
ride_details = response.json
ride_id = ride_details.get('request_id')
response = client.update_sandbox_ride(ride_id, 'accepted')
print(ride_id)