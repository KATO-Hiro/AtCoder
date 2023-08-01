# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    l, n1, n2 = map(int, input().split())
    d1 = [] * n1
    d2 = [] * n2

    for _ in range(n1):
        v1, l1 = map(int, input().split())
        d1.append([v1, l1])

    for _ in range(n2):
        v2, l2 = map(int, input().split())
        d2.append([v2, l2])

    # print(d1, d2)

    i, j = 0, 0
    ans = 0

    while i != n1 and j != n2:
        v1, l1 = d1[i]
        v2, l2 = d2[j]

        count_min = min(l1, l2)
        # print(i, j, count_min)

        if v1 == v2:
            ans += count_min

        d1[i][1] -= count_min
        d2[j][1] -= count_min

        if d1[i][1] == 0:
            i += 1
        if d2[j][1] == 0:
            j += 1

    print(ans)


if __name__ == "__main__":
    main()
