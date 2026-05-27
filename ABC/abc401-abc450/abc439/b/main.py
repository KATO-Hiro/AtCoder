# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    used = set()

    while True:
        s = list(str(n))
        m = 0

        for si in s:
            m += int(si) ** 2

        if m in used:
            print("No")
            exit()

        if m == 1:
            print("Yes")
            exit()

        used.add(m)
        n = m


if __name__ == "__main__":
    main()
