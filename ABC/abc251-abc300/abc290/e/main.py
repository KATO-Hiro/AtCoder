# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)

    def nC2(x):
        return x * (x - 1) // 2

    same = sum([nC2(count) for count in c.values()])
    ans = 0

    def delete(x):
        nonlocal same

        same -= nC2(c[x])
        c[x] -= 1
        same += nC2(c[x])

    for left in range(n):
        right = n - left - 1

        if left >= right:
            break

        ans += nC2(right - left + 1) - same

        delete(a[left])
        delete(a[right])

    print(ans)


if __name__ == "__main__":
    main()
