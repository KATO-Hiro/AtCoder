# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = 1
    count = 1

    for i in range(n - 1):
        if a[i + 1] >= a[i]:
            count += 1
        else:
            ans = max(ans, count)
            count = 1

    if count > 1:
        ans = max(ans, count)

    print(ans)


if __name__ == '__main__':
    main()
