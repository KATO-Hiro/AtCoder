# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = input().rstrip()
    t = input().rstrip()
    count = [0] * (n + 1)

    for _ in range(m):
        li, ri = map(int, input().split())
        li -= 1

        count[li] += 1
        count[ri] -= 1

    imos = list(accumulate(count))

    ans = list()

    for i, value in enumerate(imos[:-1]):
        if value % 2 == 0:
            ans.append(s[i])
        else:
            ans.append(t[i])

    print("".join(ans))


if __name__ == "__main__":
    main()
