# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    b = set(sorted(a))
    ans = 0

    for bi in b:
        count = c[bi]

        if (bi - 1) in c.keys():
            count += c[bi - 1]
        if (bi + 1) in c.keys():
            count += c[bi + 1]

        ans = max(ans, count)
    
    print(ans)


if __name__ == "__main__":
    main()
