# -*- coding: utf-8 -*-


def main():
    a, b = input().split(" ")
    sa, sb = 0, 0

    for ai in list(a):
        sa += int(ai)

    for bi in list(b):
        sb += int(bi)

    print(max(sa, sb))


if __name__ == "__main__":
    main()
