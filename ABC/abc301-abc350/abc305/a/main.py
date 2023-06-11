# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    numbers = [i for i in range(0, 100, 5)]

    for i, j in zip(numbers, numbers[1:]):
        if i <= n <= j:
            d1 = n - i
            d2 = j - n

            if d1 < d2:
                print(i)
                exit()
            else:
                print(j)
                exit()

    print(100)


if __name__ == "__main__":
    main()
