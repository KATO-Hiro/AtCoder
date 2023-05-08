# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import product

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list()

    for _ in range(m):
        ci = int(input())
        ai = list(map(int, input().split()))
        a.append(ai)

    ans = 0

    for i, pattern in enumerate(product([0, 1], repeat=m)):
        if i == 0:
            continue

        tmp = set()

        for j, pi in enumerate(pattern):
            if pi == 1:
                aj = a[j]

                for aij in aj:
                    tmp.add(aij)

        if sorted(tmp) == [i for i in range(1, n + 1)]:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
