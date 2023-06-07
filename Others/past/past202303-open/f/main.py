# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = set(map(int, input().split()))
    q = int(input())

    for _ in range(q):
        m = int(input())
        t = list(map(int, input().split()))

        count = n

        for ti in t:
            if ti not in s:
                count += 1

        print(count)


if __name__ == "__main__":
    main()
