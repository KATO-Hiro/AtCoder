# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = list(input())
    ice = [0 for _ in range(n)]
    ans = 0

    for i in range(2, n - 2):
        if s[i] == '>':
            ice[i] = ice[i - 1] + 1

    for count in ice:
        if ice == 0:
            ans += 1
        else:
            ans += 1 / (count - 1 + 2)

    kmax = max(ice)
    print(ans + (1 / (kmax + 2)) - 1)


if __name__ == '__main__':
    main()
