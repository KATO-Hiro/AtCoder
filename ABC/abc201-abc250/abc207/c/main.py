# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    lr = list()

    for i in range(n):
        ti, li, ri = map(int, input().split())
        li *= 2
        ri *= 2

        if ti == 2:
            ri -= 1
        elif ti == 3:
            li += 1
        elif ti == 4:
            li += 1
            ri -= 1

        lr.append((li, ri))

    ans = 0

    for i in range(n):
        li, ri = lr[i]

        for j in range(i + 1, n):
            lj, rj = lr[j]

            if max(li, lj) <= min(ri, rj):
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
