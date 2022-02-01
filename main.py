import time
x = int(time.time())


def random(a=6364136223846793005, c=1442695040888963407, m=2 ** 64):
    global x
    x = (a * x + c) % m
    return x


for i in range(15):
    print(random() % 10)
