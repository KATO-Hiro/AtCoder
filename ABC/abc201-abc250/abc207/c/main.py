# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    lr = list()

    for i in range(n):
        ti, li, ri = map(int, input().split())

        if ti == 2:
            ri -= 0.5
        elif ti == 3:
            li += 0.5
        elif ti == 4:
            li += 0.5
            ri -= 0.5

        lr.append((li, ri))

    ans = 0

    for i in range(n):
        li, ri = lr[i]

        for j in range(i + 1, n):
            lj, rj = lr[j]

            if li <= rj <= ri:
                ans += 1
            elif lj <= ri <= rj:
                ans += 1
            elif lj <= li and ri <= rj:
                ans += 1
            elif li <= lj and rj <= ri:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
