# -*- coding: utf-8 -*-


def main():
    n = int(input())
    d = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    a = list()

    while n:
        a.append(n % 36)
        n //= 36

    if len(a) == 0:
        print(0)
    else:
        print("".join([d[ai] for ai in a][::-1]))


if __name__ == "__main__":
    main()
