# -*- coding: utf-8 -*-


def main():
    from itertools import combinations

    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = 0

    for t1, t2 in list(combinations(range(m), 2)):
        summed = 0

        for i in range(n):
            summed += max(a[i][t1], a[i][t2])

        ans = max(ans, summed)

    print(ans)


if __name__ == '__main__':
    main()
