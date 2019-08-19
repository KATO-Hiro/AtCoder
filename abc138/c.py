# -*- coding: utf-8 -*-


def main():
    n = int(input())
    v = sorted(list(map(int, input().split())))
    ans = (v[0] + v[1]) / 2

    for i in range(2, n):
        ans = (ans + v[i]) / 2

    print(ans)


if __name__ == '__main__':
    main()
