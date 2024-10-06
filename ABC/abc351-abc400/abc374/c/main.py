# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    k = list(map(int, input().split()))
    k_sum = sum(k)
    inf = 10**18
    ans = inf

    for bit in range(1 << n):
        candidate = 0

        for i in range(n):
            if (bit >> i) & 1:
                candidate += k[i]

        ans = min(ans, max(candidate, k_sum - candidate))

    print(ans)


if __name__ == "__main__":
    main()
