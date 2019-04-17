# -*- coding: utf-8 -*-


def main():
    n = int(input())
    t = sorted([int(input()) for _ in range(n)])

    if n <= 2:
        print(max(t))
    elif n == 3:
        print(min(max(t[0] + t[1], t[2]), max(t[0] + t[2], t[1])))
    elif n == 4:
        print(min(max(t[0] + t[3], t[1] + t[2]), max(t[0] + t[2], t[1] + t[3]), max(t[0] + t[1] + t[2], t[3])))


if __name__ == '__main__':
    main()
