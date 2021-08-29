# -*- coding: utf-8 -*-


from typing import List


def lcs(a: List[str], b: List[str]) -> int:
    """Get LCS (Longest Common Subsequence).
    Args:
        a: List of numbers.
        b: List of numbers.
    Returns:
        LCS
    Landau notation: O(a_count * b_count).
    """
    n = len(a)
    m = len(b)

    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            if ai == bj:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

    return dp[n][m]


def main():
    n = int(input())
    s = list(input())
    lcs_max = 0

    for i in range(1, n):
        lcs_max = max(lcs_max, lcs(s[:i], s[i:]))

    print(n - 2 * lcs_max)


if __name__ == "__main__":
    main()
