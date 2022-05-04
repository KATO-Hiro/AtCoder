# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, y = map(int, input().split())
    total = x
    ans = 0

    while True:
        if total >= y:
            print(ans)
            exit()

        total += 10
        ans += 1


if __name__ == "__main__":
    main()
