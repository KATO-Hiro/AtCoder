# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    m = int(input())
    a = list(map(int, input().split()))
    ans = [0 for _ in range(n)]

    for i in range(m):
        ai = a[i]
        bi = list(map(int, input().split()))

        for index, bij in enumerate(bi, 1):
            if index == ai:
                ans[ai - 1] += 1
            else:
                if bij == ai:
                    ans[index - 1] += 1
                else:
                    ans[ai - 1] += 1

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
