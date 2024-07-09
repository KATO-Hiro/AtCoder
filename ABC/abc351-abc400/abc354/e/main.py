# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    patterns = 1 << n
    dp = [False] * patterns

    for bit in range(patterns):
        isWin = False

        for i in range(n):
            for j in range(i + 1, n):
                if (bit >> i) & 1 and (bit >> j) & 1:
                    ai, bi = ab[i]
                    aj, bj = ab[j]

                    if (ai == aj) or (bi == bj):
                        if not dp[bit ^ (1 << i) ^ (1 << j)]:
                            isWin = True

        dp[bit] = isWin

    if dp[patterns - 1]:
        print("Takahashi")
    else:
        print("Aoki")


if __name__ == "__main__":
    main()
