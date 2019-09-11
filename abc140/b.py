# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ans = sum(b)

    for i in range(1, n):
        if a[i] - a[i - 1] == 1:
            ans += c[a[i - 1] - 1]

    print(ans)


if __name__ == '__main__':
    main()
