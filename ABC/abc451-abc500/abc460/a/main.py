# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    ans = 0

    while True:
        _, x = divmod(n, m)
        m = x
        ans += 1

        if x == 0:
            break

    print(ans)


if __name__ == "__main__":
    main()
