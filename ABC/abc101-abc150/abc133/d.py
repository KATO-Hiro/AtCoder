# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0 for _ in range(n)]

    for index, ai in enumerate(a):
        if index % 2 == 0:
            ans[0] += ai
        else:
            ans[0] -= ai

    for i in range(n - 1):
        ans[i + 1] = 2 * a[i] - ans[i]

    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    main()
