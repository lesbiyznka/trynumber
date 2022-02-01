x = 2 ** 62


def random(a=2 ** 63, c=2 ** 62, m=2 ** 64):
    global x
    x = (a * x + c) % m
    return x


for i in range(15):
    print(random())
