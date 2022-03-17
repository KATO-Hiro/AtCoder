# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = 0

    for i in range(1, n + 1):
        if i % 15 == 0:
            continue
        elif i % 5 == 0:
            continue
        elif i % 3 == 0:
            continue
        else:
            ans += i

    print(ans)


if __name__ == "__main__":
    main()
