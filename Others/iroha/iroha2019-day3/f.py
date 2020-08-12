# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    center = (n - 2) // 2
    left = a[:center + 1]
    right = a[center + 2:]
    ans = float('inf')

    for l, r in zip(left, right):
        ans = min(ans, abs(r - l))

    print(ans)


if __name__ == '__main__':
    main()
