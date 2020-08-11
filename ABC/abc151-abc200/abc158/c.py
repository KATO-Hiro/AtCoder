# -*- coding: utf-8 -*-


def main():
    a, b = map(int, input().split())
    numbers1 = list()
    numbers2 = list()

    for i in range(1, 1250 + 1):
        if int(i * 0.08) == a:
            numbers1.append(i)

    for i in range(1, 1000 + 1):
        if int(i * 0.1) == b:
            numbers2.append(i)

    c = set(numbers1) & set(numbers2)

    if len(c) == 0:
        print(-1)
    else:
        print(min(c))


if __name__ == '__main__':
    main()
