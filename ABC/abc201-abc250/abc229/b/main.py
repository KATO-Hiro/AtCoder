# -*- coding: utf-8 -*-


def main():
    a, b = input().split()
    a = list(reversed(a))
    b = list(reversed(b))

    for ai, bi in zip(a, b):
        if int(ai) + int(bi) >= 10:
            print("Hard")
            exit()

    print("Easy")

if __name__ == "__main__":
    main()
