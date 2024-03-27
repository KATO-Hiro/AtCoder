# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)

    for value in c.values():
        if value <= 10:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
