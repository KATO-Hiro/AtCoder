# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, p, q = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0

    # まさかのO(n ** 5 / 120)が通る。
    # aが大きいので、modを取る必要がある。
    for x in range(n):
        for y in range(x + 1, n):
            tmp1 = a[x] * a[y] % p

            for z in range(y + 1, n):
                tmp2 = tmp1 * a[z] % p

                for ai in range(z + 1, n):
                    tmp3 = tmp2 * a[ai] % p

                    for bi in range(ai + 1, n):
                        tmp4 = tmp3 * a[bi] % p

                        if tmp4 == q:
                            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
