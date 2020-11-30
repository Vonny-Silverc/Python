import random

def is_valid(s, up_num):
    if s.isdigit() == True:
        if 1 <= int(s) <= up_num:
            return True
    return False

def user_play(n, up_num):
    count = 0
    while True:
        user_number = input(f'Введите число от 1 до {up_num}\n')

        if is_valid(user_number, up_num) == False:
            print(f'А может быть все-таки введем целое число от 1 до {up_num}?')
            continue
        else:
            user_number = int(user_number)

        if user_number < n:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            count += 1
        elif user_number > n:
            print('Ваше число больше загаданного, попробуйте еще разок')
            count += 1
        else:
            count += 1
            print('Вы угадали, поздравляем!')
            print(f'Число попыток = {count}')
            break

print('Добро пожаловать в числовую угадайку')
play = 'д'
while play == 'д':
    up_num = int(input('Введите пожалуйста верхнюю границу числа\n'))
    rand_number = random.randint(1, up_num)
    user_play(rand_number, up_num)
    play = input('Хотите сыграть еще? д(да)/н(нет)')

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
