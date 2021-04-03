# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    inf = float("inf")
    left = [inf for _ in range(n)]
    right = [-inf for _ in range(n)]

    for i in range(n):
        xi, ci = map(int, input().split())
        ci -= 1

        left[ci] = min(left[ci], xi)
        right[ci] = max(right[ci], xi)

    pairs = [(0, 0)]  # left, right

    for i in range(n):
        if left[i] == inf:
            continue

        pairs.append((left[i], right[i]))

    pairs.append((0, 0))

    dp = [0, 0]

    for index, pair in enumerate(pairs):
        prev = [inf, inf]
        prev, dp = dp, prev

        left, right = pair

        for j in range(2):
            if j:
                xi = pairs[index - 1][1]
            else:
                xi = pairs[index - 1][0]

            dp[0] = min(dp[0], prev[j] + (right - left) + abs(xi - right))
            dp[1] = min(dp[1], prev[j] + (right - left) + abs(xi - left))

    print(dp[1])


if __name__ == "__main__":
    main()
