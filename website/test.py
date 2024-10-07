from intasend import APIService

#API_PUBLISHABLE_KEY = 'ISPubKey_test_81c79b0c-51ca-490f-8dd0-5d34571919d3'

#API_TOKEN = 'ISSecretKey_test_5521cdd8-a331-4a23-8e03-5df8e72e3e7b'

service = APIService(token=API_TOKEN, publishable_key=API_PUBLISHABLE_KEY, test=True)

create_order = service.collect.mpesa_stk_push(phone_number='2548051068189', email='test@gmail.com', amount=100, narrative='purchase of item')


print(create_order)

