import time

x = int(time.time())


# Проверка ввода пользователя
def check_input(user_input):
    # Обработка исключения
    try:
        if 1 <= int(user_input) <= 10:
            return True
    except ValueError:
        return False
    return False


# LCG генератор чисел
def random(a=6364136223846793005, c=1442695040888963407, m=2 ** 64):
    global x
    x = (a * x + c) % m
    return x