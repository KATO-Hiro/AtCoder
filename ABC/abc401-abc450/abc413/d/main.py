# -*- coding: utf-8 -*-


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a, key=lambda x: abs(x))
    ok = True

    for i in range(n):
        if i + 2 >= n:
            break

        if a[i + 1] ** 2 != a[i] * a[i + 2]:
            ok = False
            break

    if ok:
        return "Yes"

    # コーナーケース: r = -1
    if abs(a[0]) == abs(a[-1]):
        diff = a.count(a[0]) - a.count(-a[0])

        if abs(diff) <= 1:
            return "Yes"

    return "No"


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        ans = solve()
        print(ans)


if __name__ == "__main__":
    main()
