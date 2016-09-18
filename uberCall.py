from uber_rides.session import Session
session = Session(server_token='60KIlvmpVK8JWNiNvau69NTqziJsT-0KM9e0Hlfb')
from uber_rides.client import UberRidesClient
client = UberRidesClient(session)
response = client.get_products(37.77, -122.41)
products = response.json.get('products')
print("this ran")

def returnProducts(): 
	print('~~~~~~~~~~~~~')
	print(products)
	print('~~~~~~~~~~~~~')


# client = UberRidesClient(session, sandbox_mode=True)
# response = client.request_ride(
#     product_id=products[0].get('product_id'),
#     start_latitude=37.77,
#     start_longitude=-122.41,
#     end_latitude=37.79,
#     end_longitude=-122.35,
# )
# ride_details = response.json
# ride_id = ride_details.get('request_id')
# response = client.update_sandbox_ride(ride_id, 'accepted')
# print(ride_id)

def getAuthenticationURL(): 
	from uber_rides.auth import AuthorizationCodeGrant
	auth_flow = AuthorizationCodeGrant(
	    'Xy07019vgK4SdQGGxPYFOjUVBRbskX0Z',
	    ['profile'],
	    'cgN1x77XOhdLP7LADi1jO0CARk5ce9v11T8ALtZ9',
	    'http://localhost:5000/callback',
	)
	auth_url = auth_flow.get_authorization_url()
	return auth_url

def beginTexting(ac, pn): 
	print("this is the phone number " + pn) 
	print("this is the access ccode " + ac)

	