from engine import *


# Получение слова
def get_word():
    num_lines = sum(1 for line in open('gibbet.txt'))
    num = random() % num_lines
    txt = open('gibbet.txt', 'r', encoding="utf-8")

    i=0
    for line in txt:
        if i == num:
            txt.close()
            return line
        i+=1


# Основной игровой цикл
def gibbet():
    word = get_word()

    # Количество букв
    count = len(word)
    print(f"В слове всего {count} букв, попробуй угадать")

    attempts = 12

    while attempts > 0:
        # Вывод угаданной буквы
        for symbol in word:
            if symbol.isupper():
                print(symbol, end='')
            else:
                print('-', end='')

        inp = input("Введите букву\n>>>")
        char = word.find(inp)
        if char == -1:
            attempts -= 1
        else:
            # Заглавная буква по индексу
            word = word[:char] + word[char].upper() + word[char+1:]
            print("Вы угадали букву!")



