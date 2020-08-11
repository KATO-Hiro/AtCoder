# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0

    for i in range(n):
        left = min(a[i], b[i])
        ans += left
        b[i] -= left

        right = min(a[i + 1], b[i])
        ans += right
        a[i + 1] -= right

    print(ans)


if __name__ == '__main__':
    main()
