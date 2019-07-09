# -*- coding: utf-8 -*-


def main():
    l, r = map(int, input().split())
    mod = 2019
    ans = mod
    r = min(r, l + mod)

    for i in range(l, r):
        for j in range(i + 1, r + 1):
            candidate = i * j
            candidate %= mod
            ans = min(ans, candidate)

    print(ans)


if __name__ == '__main__':
    main()
