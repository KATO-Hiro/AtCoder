# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict

    n = int(input())
    d = defaultdict(str)

    for i in range(n):
        before, after = input().split()
        d[before] = after

    m = int(input())
    keys = d.keys()
    ans = ''

    for j in range(m):
        s = input()

        if s in keys:
            ans += d[s]
        else:
            ans += s

    print(ans)


if __name__ == '__main__':
    main()
