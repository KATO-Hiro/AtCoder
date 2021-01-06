# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    ans = 1
    freq = [0 for _ in range(n + 1)]
    freq[0] = 3

    for ai in a:
        if freq[ai] == 0:
            print(0)
            exit()

        ans *= freq[ai]
        ans %= mod

        freq[ai] -= 1
        freq[ai + 1] += 1

    print(ans)


if __name__ == "__main__":
    main()
