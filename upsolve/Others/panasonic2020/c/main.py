# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c = map(int, input().split())
    d = c - (a + b)

    # 1ケースWAの原因は、d > 0であることをチェックしてなかったため
    if d > 0 and (4 * a * b) < d**2:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
