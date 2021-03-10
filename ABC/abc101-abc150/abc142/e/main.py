# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    keys = list()

    for i in range(m):
        ai, _ = map(int, input().split())
        c = list(map(lambda x: int(x) - 1, input().split()))

        key_set = 0

        for ci in c:
            key_set |= 1 << ci

        keys.append((key_set, ai))

    dp = [float("inf") for _ in range(1 << n)]
    dp[0] = 0

    for current_set in range(1 << n):
        for current_key in range(m):
            new_set = current_set | keys[current_key][0]
            cost = dp[current_set] + keys[current_key][1]
            dp[new_set] = min(dp[new_set], cost)

    ans = dp[-1]

    if ans == float("inf"):
        ans = -1

    print(ans)


if __name__ == "__main__":
    main()
