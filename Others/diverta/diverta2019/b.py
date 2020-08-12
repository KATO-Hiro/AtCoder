# -*- coding: utf-8 -*-


def main():
    r, g, b, n = map(int, input().split())
    comb = list()
    ans = 0

    for i in range(3000 + 1):
        for j in range(3000 + 1):
            comb.append(r * i + g * j)

    for c in comb:
        if (n - c) >= 0 and (n - c) % b == 0:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
