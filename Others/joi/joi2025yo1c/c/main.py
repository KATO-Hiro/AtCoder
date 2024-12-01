# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = int(input())
    b = int(input())
    ans = 0

    for i in range(1, n + 1):
        if i % a != 0 and i % b != 0:
            continue
        if i % a == 0 and i % b == 0:
            continue

        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
