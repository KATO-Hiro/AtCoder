# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import product

    input = sys.stdin.readline

    n = int(input())
    f = [list(map(int, input().split())) for _ in range(n)]
    p = [list(map(int, input().split())) for _ in range(n)]
    t = 10
    inf = -(10**18)
    ans = inf

    for bit in range(1, 1 << t):
        summed = 0

        for i in range(n):
            count = 0

            # 自分の店が営業している(bitが立っている)ときだけ、i番目の店と比較
            for k in range(t):
                if (bit >> k) & 1:
                    count += f[i][k]

            summed += p[i][count]

        ans = max(ans, summed)

    print(ans)


if __name__ == "__main__":
    main()
