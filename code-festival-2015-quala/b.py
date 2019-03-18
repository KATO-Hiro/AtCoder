# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0

    for index, ai in enumerate(a):
        power = n - index - 1
        ans += pow(2, power) * a[index]

    print(ans)


if __name__ == '__main__':
    main()
