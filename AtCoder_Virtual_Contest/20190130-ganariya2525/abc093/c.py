# -*- coding: utf-8 -*-


def main():
    a, b, c = map(int, input().split())
    maximum = max(a, b, c)
    summed = sum([a, b, c])

    while True:
        diff = maximum * 3 - summed

        if diff % 2 == 0:
            print(diff // 2)
            exit()
        else:
            maximum += 1


if __name__ == '__main__':
    main()
