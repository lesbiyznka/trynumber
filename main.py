from gibbet import *
from trynumber import *


def main():
    while True:
        choice = int(input("Выберите игру:\n1. Угадай число\n2. Виселица\n0. Выход\n>>>"))
        if choice == 1:
            try_number()
        elif choice == 2:
            gibbet()
        elif choice == 0:
            return
        else:
            print("Такой игры нет в списке")


# Основной цикл игровой программы
if __name__ == "__main__":
    main()






