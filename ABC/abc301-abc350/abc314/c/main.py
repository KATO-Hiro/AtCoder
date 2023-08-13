# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = input().rstrip()
    c = list(map(int, input().split()))
    d = defaultdict(list)

    for i, ci in enumerate(c):
        d[ci].append([i, s[i]])

    # print(d)
    ans = [""] * n

    for key, values in d.items():
        size = len(values)
        # tmp = list()
        # print(key, values, size)

        for i, (id, value) in enumerate(values):
            # print(id, value)
            nid = (i + 1) % size
            ans[values[nid][0]] = value
            # tmp.append([values[nid][0], value])

        # print(tmp)
    print("".join(ans))


if __name__ == "__main__":
    main()
