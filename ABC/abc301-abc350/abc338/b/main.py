# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter, defaultdict

    input = sys.stdin.readline
    d = defaultdict(list)

    s = input().rstrip()
    c = Counter(s)
    # print(c)

    for key, value in c.items():
        d[value].append(key)

    # print(d)
    key_max = max(d.keys())
    print(sorted(d[key_max])[0])


if __name__ == "__main__":
    main()
