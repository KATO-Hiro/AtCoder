# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    l = int(input())
    l -= 1
    ans = 1

    for i in range(1, 12):
        ans *= l - i + 1
        ans //= i
        # print(l - i + 1, i)

    print(ans)


if __name__ == "__main__":
    main()
