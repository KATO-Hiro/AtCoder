# -*- coding: utf-8 -*-


def count_combinations(n, k, mod):
    # See:
    # https://beta.atcoder.jp/contests/abc034/submissions/3410655
    if k > n - k:
        return count_combinations(n, n - k, mod)

    ans = 1

    for i in range(1, k + 1):
        ans *= n - i + 1
        ans %= mod
        ans *= pow(i, mod - 2, mod)
        ans %= mod

    return ans


def main():
    w, h = map(int, input().split())
    n = w + h - 2
    k = min(w, h)
    print(count_combinations(n, k - 1, 10 ** 9 + 7))


if __name__ == '__main__':
    main()
