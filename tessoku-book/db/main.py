# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline


    a, b = map(int, input().split())
    mod = 10 ** 9 + 7
    ans = pow(a, b, mod)
    print(ans)


if __name__ == "__main__":
    main()
