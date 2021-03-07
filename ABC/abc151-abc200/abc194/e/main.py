# -*- coding: utf-8 -*-


def main():
    from collections import Counter

    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = Counter(a[:m])
    ans = 0

    while c[ans]:
        ans += 1

    for i in range(m, n):
        c[a[i]] += 1
        c[a[i - m]] -= 1

        if c[a[i - m]] == 0:
            ans = min(ans, a[i - m])

    print(ans)


if __name__ == "__main__":
    main()
