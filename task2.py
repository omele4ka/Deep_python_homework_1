# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def is_simple_num(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


number = int(input('Введите целое число от 1 до 100000: '))

if number < 1 or number > 100000:
    print('Введите число в заданном диапазоне: от 1 до 100000')
else:
    if is_simple_num(number):
        print('Это простое число')
    else:
        print('Это составное число')