# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
from random import randint

print('Давай сыграем')
print('У тебя 10 попыток')
def guess_num():
    hidden_number = randint(0, 1001)
    count = 10
    while count > 0:
        num = int(input('Введи число от 0 до 1000: '))
        if num < hidden_number:
            print('Больше')
        elif num > hidden_number:
            print('Меньше')
        else:
            print('Ты угадал!')
            break
        count -= 1

    if count == 0:
        print(f'Ходы закончились! Было загадано число {hidden_number}')

guess_num()
