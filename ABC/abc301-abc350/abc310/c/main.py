# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    n = int(input())
    s = [input().rstrip() for _ in range(n)]
    c = Counter(s)
    d = Counter([si[::-1] for si in s])
    used = set()
    ans = set()

    for key in c.keys():
        if len(key) == 1:
            ans.add(key)
            used.add(key)

        if key in used:
            continue

        rev_key = key[::-1]

        if rev_key in d.keys():
            used.add(rev_key)

        ans.add(key)
        used.add(key)

    # print(d)
    print(len(ans))


if __name__ == "__main__":
    main()
