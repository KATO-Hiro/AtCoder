# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    count = [0] * 110

    for ai in a:
        for j in range(min(ai + 1, 101)):
            count[j] += 1

    ans = 0

    for i in range(101):
        if count[i] >= i:
            ans = i

    print(ans)


if __name__ == "__main__":
    main()
