# -*- coding: utf-8 -*-


def main():
    n = int(input())
    diff = 2025 - n

    for i in range(1, 10):
        p, q = divmod(diff, i)

        if q == 0 and p <= 9:
            print(str(i) + ' x ' + str(p))


if __name__ == '__main__':
    main()
