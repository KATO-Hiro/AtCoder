# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())

    k_rev = int(str(k)[::-1])
    ans = set()

    # f(k) = k にならない
    if k > k_rev:
        print(0)
        exit()

    while k <= n or k_rev <= n:
        if n >= k:
            ans.add(k)
        if n >= k_rev:
            ans.add(k_rev)

        k *= 10
        k_rev *= 10

    print(len(ans))


if __name__ == "__main__":
    main()
