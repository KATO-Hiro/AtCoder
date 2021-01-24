# -*- coding: utf-8 -*-


def main():
    n = int(input())
    dp = [[0 for _ in range(n + 1)] for _ in range(2)]
    dp[0][0] = 1
    dp[1][0] = 1

    for i in range(n):
        si = input()

        for j in range(2):
            for x in range(2):
                nj = j

                if si == "AND":
                    nj &= x
                else:
                    nj |= x

                dp[nj][i + 1] += dp[j][i]

    print(dp[1][n])


if __name__ == "__main__":
    main()
