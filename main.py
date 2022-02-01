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


# Игра "угадай число"
def try_number():
    while True:
        print("Если угадай число от 1 до 10, для выхода напиши exit\n>>>", end='')
        n = input()

        # Выход из игры
        if n == "exit":
            break

        if not check_input(n):
            print("хуню ввел")
            continue

        num_rand = random() % 10 + 1

        # Проверка везения
        if num_rand == int(n):
            print("Угадал!")
        else:
            print(f"НЕ УГАДАЛ!!!!!!\nЗагаданное число ---> {num_rand} Твое число ---> {n}")


# Основной цикл игровой программы
if __name__ == "__main__":
    try_number()






