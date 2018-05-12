друзьяВаси = {'Петя'}
друзьяПети = {'Вася'}

def mainMenu():
    print('Введите номер действия:  \n'
          '1 - Редактировать друзей \n'
          '2 - Просмотреть друзей   \n')
    mainMenu = int(input())
    if mainMenu == 1:
        editMenu()

mainMenu()

def editMenu():
        print('Введите номер действия:     \n'
              '1 - Добавить друга для Васи \n'
              '2 - Добавить друга для Пети \n'
              '3 - Удалить друга у Васи    \n'
              '4 - Удалить друга у Пети    \n')

        editMenu = int(input())
        print()
        if editMenu == 1:
            repeatEdit()

def repeatEdit():
    newVFriend = input('Введите имя нового друга для Васи: ')
    print('(Напишите "stop" если хотите прекратить ввод)')

    if newVFriend == 'stop':
        mainMenu()

    elif newVFriend != 'stop':
        друзьяВаси.add(newVFriend)
        repeatEdit()
'''
def viewMenu():
    if mainMenu == 2:
        print('Введите номер действия:                   \n'
              '1 - Просмотреть друзей у Васи             \n'
              '2 - Просмотреть друзей у Пети             \n'
              '3 - Просмотреть общих друзей              \n'
              '4 - Просмотреть друзей которых нет у Васи \n'
              '5 - Просмотреть друзей которых нет у Пети \n')

        viewMenu = int(input())
        print()
'''