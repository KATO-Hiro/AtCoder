# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, a, b = map(int, input().split())

    ans1 = x + 1
    ans2 = ans1 * (a + b)
    ans3 = ans2 ** 2
    ans4 = ans3 - 1

    print(ans1)
    print(ans2)
    print(ans3)
    print(ans4)


if __name__ == "__main__":
    main()
