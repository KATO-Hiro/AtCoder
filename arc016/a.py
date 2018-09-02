# -*- coding: utf-8 -*-


def main():
    n, m = map(int, input().split())

    for i in range(1, n + 1):
        if i != m:
            print(i)
            exit()


if __name__ == '__main__':
    main()
