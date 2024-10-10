# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x = int(input())
    ans = 0

    for i in range(x):
        if i % 2 == 0:
            ans += 3
        else:
            ans -= 2

    print(ans)


if __name__ == "__main__":
    main()
