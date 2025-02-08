# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    n = int(input())
    k = list()
    a = list()

    for _ in range(n):
        ki, *ai = list(map(int, input().split()))

        k.append(ki)
        c = Counter(ai)
        a.append(c)

    ans = 0

    for i in range(n):
        ki = k[i]
        ai = a[i]

        for j in range(i + 1, n):
            kj = k[j]
            aj = a[j]

            candidate = 0
            common = set(ai.keys()) & set(aj.keys())

            for ci in common:
                candidate += (ai[ci] / ki) * (aj[ci] / kj)

            ans = max(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()
