# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    k = int(input())
    ans = 1

    for i in range(2, 10**5 + 1):
        ans *= i

        if ans % k == 0:
            print(i)
            exit()


if __name__ == "__main__":
    main()
