# -*- coding: utf-8 -*-


def main():
    from collections import Counter

    n = int(input())
    c = Counter()
    ans = 0

    for i in range(n):
        si = sorted(input())
        c[''.join(map(str, si))] += 1

    for idx, ci in c.items():
        ans += ci * (ci - 1) // 2

    print(ans)


if __name__ == '__main__':
    main()
