import requests
import time

api_url='https://api.vk.com/method/'
method=('messages.send','none')

token=input('Введите Ваш токен: ')
peer_id=input('Введите id пользователя, которому Вы хотите написать: ')
message_text=input('Введите отправляемый текст: ')

#method_number = 'none'
#todo: make other methods.
    
def message_send():
    data = requests.get(api_url+method[0],
    {'peer_id':peer_id,'message':message_text,'v':'5.74',
     'access_token':token})
    return data.json()

message_send()
