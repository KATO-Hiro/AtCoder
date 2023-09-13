# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    if n % 2 == 1:
        print(0)
        exit()

    ans = n // 10
    count = ans

    while count // 5 > 0:
        count //= 5
        ans += count

    print(ans)


if __name__ == "__main__":
    main()
