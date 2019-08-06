# -*- coding: utf-8 -*-


def main():
    n = int(input())

    if n % 2 == 0:
        print(n // 2, n, n)
    else:
        for i in range(1, 3500 + 1):
            for j in range(1, 3500 + 1):
                if n % (i * j) == 0:
                    print(n // (i * j))
                    if (n // (i * j)) * (i + j) + i * j == 4:
                        if n // (i * j) > 0:
                            print(i, j, n // (i * j))
                            exit()


if __name__ == '__main__':
    main()
