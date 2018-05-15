import requests
import time

api_url='https://api.vk.com/method/'
method=('messages.send','polls.create','wall.post')

def back_to_operation():
    operation()

def back_to_main():
    main()

def back_to_error():
    error()

def back_to_poll_create():
    poll_create()

def back_to_message_send():
    message_send()

def error():
    error_choice=input('\nОшибка.\n'
                       '1 - Назад\n'
                       '2 - Главная\n'
                       'Выберите действие: ')
    if error_choice=='1':
        back_to_operation()
    elif error_choice=='2':
        back_to_main()
    else:
        back_to_error()

def message_send():
    peer_id=input('\nВведите id пользователя, которому Вы хотите написать: ')
    message=input('\nВведите отправляемый текст: ') 
    data=requests.get(api_url+method[0],
    {'peer_id':peer_id,'message':message,'v':'5.74',
     'access_token':access_token})
    repeat_message_send=input('\n1 - Отправить сообщение еще раз\n'
                              '2 - Назад\n'
                              'Выбрать действие: ')
    if repeat_message_send=='1':
        back_to_message_send()
    elif repeat_message_send=='2':
        back_to_operation()
    else:
        error()

def poll_create():
    question=input('\nВведите заголовок опроса: ')
    add_answer1=input('\nВведите первый вариант ответа: ')
    add_answer2=input('\nВведите второй вариант ответа: ')
    data=requests.get(api_url+method[1],
    {'question':question,'add_answers':'["'+add_answer1+'","'+add_answer2+'"]','v':'5.74',
     'access_token':access_token})
    data=data.json()
    poll_owner_id=data['response']['id']
    data=requests.get(api_url+method[2],
    {'attachments':'poll'+str(poll_owner_id)+'_'+str(poll_owner_id),'v':'5.74',
     'access_token':access_token})
    repeat_poll_create=input('\n1 - Создать опрос еще раз\n'
                             '2 - Назад\n'
                             'Выбрать действие: ')
    if repeat_poll_create=='1':
        back_to_poll_create()
    elif repeat_poll_create=='2':
        back_to_operation()
    else:
        error()

def operation():
    operation=input('\n1 - Отправить сообщение\n'
                    '2 - Создать опрос\n'
                    '3 - В разработке...\n'
                    'Выберите действие: ')
    if operation=='1':
        message_send()
    elif operation=='2':
        poll_create()
    else:
        error()

def main():
    main=input('!ВАЖНО!\n'
               'Если Вы используете приложение это впервые - введите 1\n'
               '\nГлавная\n'
               '1 - Получить токен\n'
               '2 - Ввести токен\n'
               'Выберите действие: ')
    if main=='1':
        global access_token
        print('\nПожалуйста, для корректной работы выполните последующие шаги, это не отнимет у Вас много времени.\n')
        app_id=input('Введите id Вашего приложения: ')
        print('\nПерейдите по следующей ссылке и разрешите доступ:\n\n'
              'https://oauth.vk.com/authorize?client_id='+app_id+
              '&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=messages,wall,offline&response_type=token&v=5.52\n')
        access_token=input('Скопируйте токен и вставьте сюда: ')
        operation()
    elif main=='2':
        access_token=input('\nВведите уже имеющийся токен: ')
        operation()
    else:
        print('\nОшибка. Переход на главную...\n')
        time.sleep(0.8)#Просто задержка по приколу (вообще бесполезная часть кода) :).
        back_to_main()
main()
