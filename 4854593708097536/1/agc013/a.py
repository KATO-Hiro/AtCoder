# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    diff = [0] * (n - 1)
    ans = 1

    for i in range(n - 1):
        diff[i] = a[i + 1] - a[i]

    count = 0

    for k in range(n - 2):
        if diff[k + 1] * diff[k] < 0:
            count += 1
            ans += 1
            print(count, ans)

    print(ans)


if __name__ == '__main__':
    main()
