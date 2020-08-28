# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    max_a = max(a)

    for index, ai in enumerate(a, 1):
        if ai == max_a:
            print(index)
            exit()


if __name__ == '__main__':
    main()
