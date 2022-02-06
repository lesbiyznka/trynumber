from engine import *


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