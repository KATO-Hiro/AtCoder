# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    acc_a = list(accumulate([0] + a))
    ans = 0

    for l in range(n):
        for r in range(l, n):
            summed = acc_a[r + 1] - acc_a[l]
            ok = True

            for i in range(l, r + 1):
                if summed % a[i] == 0:
                    ok = False
                    break

            if ok:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
