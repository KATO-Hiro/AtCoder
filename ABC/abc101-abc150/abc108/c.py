# -*- coding: utf-8 -*-


def main():
    n, k = list(map(int, input().split()))
    ans = 0
    count1 = 0
    count2 = 0

    for i in range(1, n + 1):
        if i % k == 0:
            count1 += 1
        if i % k == k // 2:
            count2 += 1

    ans += count1 ** 3

    if k % 2 == 0:
        ans += count2 ** 3

    print(ans)


if __name__ == '__main__':
    main()
