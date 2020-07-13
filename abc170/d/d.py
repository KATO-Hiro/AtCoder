# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    a = sorted(set(list(map(int, input().split()))))
    m = len(a)
    max_value = 10 ** 6
    dp = [False for _ in range(max_value + 1)]

    if 1 in a or m == 1:
        print(0)
        exit()

    for ai in a:
        dp[ai] = True

    for ai in a:
        for i in range(2 * ai, max_value + 1, ai):
            if dp[i]:
                dp[i] = False

    print(sum(dp))


if __name__ == '__main__':
    main()
