# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter
    from itertools import accumulate

    input = sys.stdin.readline

    n, l = map(int, input().split())
    d = list(map(int, input().split()))

    if l % 3 != 0:
        print(0)
        exit()

    d2 = list(accumulate(d, initial=0))
    dmod = [x % l for x in d2]
    freq = Counter(dmod)
    l3 = l // 3
    ans = 0

    for i in range(l3):
        a, b, c = i, i + l3, i + 2 * l3
        ans += freq[a] * freq[b] * freq[c]

    print(ans)


if __name__ == "__main__":
    main()
