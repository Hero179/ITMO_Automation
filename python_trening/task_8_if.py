num = 3

if num >= 0:
    print('Число больше либо равно 0')
else:
    print('Число отрицательное')


def task_yes_no(str_1, str_2):
    if str_1 in str_2:
        print('ДА')
    else:
        print('НЕТ')

task_yes_no(str_1='test1', str_2='test1')

num_float = 0

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Отрицательное число')

permit_print = True

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')

def student_rank(yea_of_study):
    if yea_of_study == 1 or yea_of_study == 2 or yea_of_study == 3 or yea_of_study == 4:
        print('Вы бакалавр')
    elif yea_of_study in range (5, 7):
        print('Вы магистр')
    elif 7 <= yea_of_study <= 9:
        print('Вы аспирант')
    else:
        print('Введите корректный год обучения')

student_rank(10)

num = 3

if num > 100 or  num < -100:
    print('-')
else:
    print('+')