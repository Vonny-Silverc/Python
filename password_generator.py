import random

def generate_password(len_p, ch):
    res_password = ''
    for i in range(len_p):
        res_password += random.choice(ch)
    return res_password


digits = '23456789'
lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKMNPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
exc_symbol = 'il1Lo0O'
chars = ''

print('Добро пожаловать в генератор паролей!')
cnt_password = int(input('Введите количество паролей\n'))
len_password = int(input('Введите длинну пароля\n'))
digit_on = input('Включить ли цифры?(y/n)\n')
up_alpha_on = input('Включить ли прописные буквы?(y/n)\n')
lower_alpha_on = input('Включить ли строчные буквы?(y/n)\n')
chr_on = input('Включать ли символы "!#$%&*+-=?@^_"? (y/n)\n')
exc_on = input('Исключать ли неоднозначные символы "il1Lo0O"? (y/n)\n')

if digit_on[0].lower() == 'y':
    chars += digits
if up_alpha_on[0].lower() == 'y':
    chars += uppercase_letters
if lower_alpha_on[0].lower() == 'y':
    chars += lowercase_letters
if chr_on[0].lower() == 'y':
    chars += punctuation
if exc_on[0].lower() == 'n':
    chars += exc_symbol

for _ in range(cnt_password):
    print(generate_password(len_password, chars))
