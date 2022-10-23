from random import randint

n = randint(2, 20)
x = randint(-10 ** 4, 10 ** 4)
y = randint(-10 ** 4, 10 ** 4)
a = [randint(1, 10) for _ in range(n)]

print(n, x, y)
print(*a)