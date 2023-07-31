# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = [-1] * (1 << n)
    b = [(ai, i) for i, ai in enumerate(a)]

    for round in range(1, n + 1):
        size = len(b)
        tmp = list()

        if round == n:
            first, x = b[0]
            second, y = b[1]

            ans[x] = round
            ans[y] = round
        else:
            for i in range(size // 2):
                first, x = b[2 * i]
                second, y = b[2 * i + 1]

                if first > second:
                    tmp.append(b[2 * i])
                    ans[y] = round
                else:
                    tmp.append(b[2 * i + 1])
                    ans[x] = round

            b, tmp = tmp, b

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
