# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    upper = 2 * 10 ** 5 + 1
    c = Counter(a)
    ans = 0

    # See:
    # https://atcoder.jp/contests/abc249/submissions/31175801
    for i in range(1, upper):
        k = 0

        for j in range(i, upper, i):
            k += 1
            ans += c[i] * c[j] * c[k]

    print(ans)


if __name__ == "__main__":
    main()
