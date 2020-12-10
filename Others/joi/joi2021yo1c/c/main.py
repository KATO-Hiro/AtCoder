# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    count = 0

    for ai in a:
        for bi in b:
            if ai <= bi:
                count += 1

    print(count)


if __name__ == "__main__":
    main()
