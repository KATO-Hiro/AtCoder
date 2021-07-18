# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    d = Counter(c[:k])
    ans = len(d)

    for j in range(n):
        if j + k == n:
            break

        d[c[j]] -= 1

        if d[c[j]] == 0:
            del d[c[j]]

        d[c[j + k]] += 1
        
        ans = max(ans, len(d))

    print(ans)


if __name__ == "__main__":
    main()
