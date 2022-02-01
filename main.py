import time
x = int(time.time())

# Проверка ввода пользователя
def check_input(user_input):
    if 1 <= int(user_input) <= 10:
        return True
    return False


# LCG генератор чисел
def random(a=6364136223846793005, c=1442695040888963407, m=2 ** 64):
    global x
    x = (a * x + c) % m
    return x

# Основной игровой цикл
while True:
    print("Если угадай число от 1 до 10")

    n = input()


    if not check_input(n):
        print("хуню ввел")
        continue

    num_rand = random() % 10 + 1

    # Проверка везения
    if num_rand == int(n):
        print("Угадал!")
    else:
        print("НЕ УГАДАЛ!!!!!!")
        print(f"Загаданное число ---> {num_rand} Твое число ---> {n}")






