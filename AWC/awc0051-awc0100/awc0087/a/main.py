# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    t, x, y = map(int, input().split())
    a = input().rstrip()
    b = input().rstrip()
    ans = 0

    for ai, bi in zip(a, b):
        if ai == "L":
            x -= 1
        elif ai == "R":
            x += 1

        if bi == "L":
            y -= 1
        elif bi == "R":
            y += 1

        if x == y:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
