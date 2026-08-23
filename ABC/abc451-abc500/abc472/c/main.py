# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    summed = 0
    ans = []

    for i in range(m):
        ai = a[i]

        if summed + ai > k:
            a[i] = 0
            ans.append("No")
        else:
            summed += ai
            ans.append("Yes")

    for j in range(m, n):
        aj = a[j]
        candidate = summed + aj - a[j - m]

        if candidate > k:
            a[j] = 0
            ans.append("No")
            summed -= a[j - m]
        else:
            summed = candidate
            ans.append("Yes")

    for ans_i in ans:
        print(ans_i)


if __name__ == "__main__":
    main()
