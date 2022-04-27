a=int(input('Введите первое число: '))
b=int(input('Введите второе число: '))

print('''Выберете действие 
         1-Умножить
         2-Разделить
         3-Прибавить
         4-Отнять   
         5-Возвести в степень''')
action=int(input('Какое действие: '))

if action == 1:
    print(a*b)
elif action == 2:
    print(a/b)
elif action == 3:
    print(a+b)
elif action == 4:
    print(a-b)
elif action == 5:
    print(a**b)
else:
    print('none')