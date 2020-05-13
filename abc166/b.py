# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n, k = map(int, input().split())
    count = [[] for _ in range(n)]

    for i in range(k):
        di = int(input())
        a = list(map(int, input().split()))

        for ai in a:
            count[ai - 1].append(i)

    ans = 0

    for c in count:
        if len(c) == 0:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
