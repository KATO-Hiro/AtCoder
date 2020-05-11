# -*- coding: utf-8 -*-


def main():
    from itertools import product
    import sys
    input = sys.stdin.readline

    n, m, x = map(int, input().split())
    c = list()
    a = list()

    for i in range(n):
        bi = list(map(int, input().split()))

        ci = bi[0]
        c.append(ci)

        ai = bi[1:]
        a.append(ai)

    ans = float('inf')

    for p in list(product(range(2), repeat=n)):
        tmp = [0 for _ in range(m)]
        cost = 0

        for index, pi in enumerate(p):
            if pi == 1:
                for idx, aii in enumerate(a[index]):
                    tmp[idx] += aii

                cost += c[index]

        is_ok = True

        for t in tmp:
            if t < x:
                is_ok = False
                break

        if is_ok:
            ans = min(ans, cost)

    if ans == float('inf'):
        print(-1)
    else:
        print(ans)


if __name__ == '__main__':
    main()
