# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = list()

    for i, (ai, aj) in enumerate(zip(a, a[1:])):
        if abs(ai - aj) == 1:
            ans.append(ai)

            continue

        if ai < aj:
            for i in range(ai, aj):
                ans.append(i)
        elif ai > aj:
            for i in range(ai, aj, -1):
                ans.append(i)

    ans.append(a[-1])
    print(*ans)


if __name__ == "__main__":
    main()
