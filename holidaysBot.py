def repeat():
    print(
          'Введите номер месяца: \n'
          '1 - Январь            \n'
          '2 - Февраль           \n'
          '3 - Март              \n'
          '4 - Апрель            \n'
          '5 - Май               \n'
          '6 - Июнь              \n'
          '7 - Июль              \n'
          '8 - Август            \n'
          '9 - Сентябрь          \n'
          '10 - Октябрь          \n'
          '11 - Ноябрь           \n'
          '12 - Декабрь          \n'
         )

    month = int(input())
    print()

    if 1 <= month <= 12:
        if month == 1:
            print('С 1 - 2 января - Новый Год                  \n')
        elif month == 2:
            print('Нет государственных праздников              \n')
        elif month == 3:
            print('8 марта - Международный Женский День        \n'
                  '21 - 23 марта - Наурыз Мейрамы              \n')
        elif month == 4:
            print('Нет государственных праздников              \n')
        elif month == 5:
            print('1 мая - Праздник Единства Народа Казахстана \n'
                  '7 мая - День Защитника Отечества            \n'
                  '9 мая - День Победы                         \n')
        elif month == 6:
            print('Нет государственных праздников              \n')
        elif month == 7:
            print('6 июля - День Столицы                       \n')
        elif month == 8:
            print('30 августа - День Конституции РК            \n')
        elif month == 9:
            print('Нет государственных праздников              \n')
        elif month == 10:
            print('Нет государственных праздников              \n')
        elif month == 11:
            print('Нет государственных праздников              \n')
        elif month == 12:
            print('1 декабря - День Первого Президента РК      \n'
                  '16 декабря - День Независимости РК          \n')
    else:
        print('Ты где такой месяц нашел? ;)                    \n')

    repeat()

repeat()