# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    is_logged_in = False
    ans = 0

    for _ in range(n):
        si = input().rstrip()

        if si == "login":
            is_logged_in = True
        elif si == "logout":
            is_logged_in = False

        if not is_logged_in and si == "private":
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
