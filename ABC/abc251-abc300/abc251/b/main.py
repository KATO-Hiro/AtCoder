# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    ans = set()

    for i in range(n):
        if a[i] <= w:
            ans.add(a[i])

        for j in range(i + 1, n):
            summed2 = a[i] + a[j]

            if summed2 <= w:
                ans.add(summed2)

            for k in range(j + 1, n):
                summed3 = a[i] + a[j] + a[k]

                if summed3 <= w:
                    ans.add(summed3)

    print(len(ans))


if __name__ == "__main__":
    main()
