word = "бебра"

# Количество букв
quant = len(word)


# Проверка ввода пользователя
def check_input(user_input):
    if user_input == "да":
        return True
    else:
        return False
    return False

# Основной игровой цикл
while True:
    print(f"Хочешь сыграть в виселицу? Если хочешь пиши да\n>>>", end='')
    n = input()


    if not check_input(n):
        print("Попробуй еще")
        continue

    if check_input(n):
        print(f"В слове всего {quant} букв, попробуй угадать)\n>>>", end='')
        inp = input()
