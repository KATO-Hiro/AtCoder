# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    height = a[0]
    ans = 0

    for i in range(1, n):
        if height > a[i]:
            ans += height - a[i]
        else:
            height = a[i]

    print(ans)


if __name__ == '__main__':
    main()
