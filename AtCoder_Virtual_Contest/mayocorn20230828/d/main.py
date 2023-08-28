# -*- coding: utf-8 -*-


def mex(ai, aj, ak):
    return min(set([ai, aj, ak]) ^ set([i for i in range(4)]))


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    s = input().rstrip()
    m, x = [0] * 3, [0] * 3

    # Eを固定 + 累積和で高速化
    for ak, sk in zip(a, s):
        if sk == "X":
            x[ak] += 1

    ans = 0

    for aj, sj in zip(a, s):
        if sj == "M":
            m[aj] += 1
        elif sj == "E":
            for ai in range(3):
                for ak in range(3):
                    ans += mex(ai, aj, ak) * m[ai] * x[ak]
        elif sj == "X":
            x[aj] -= 1

    print(ans)


if __name__ == "__main__":
    main()
