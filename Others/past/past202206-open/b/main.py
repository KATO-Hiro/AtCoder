# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    n = len(s)
    c = Counter()

    for i in range(n - 1):
        si = s[i:i + 2]
        c[si] += 1
    
    count_max = max(c.values())
    ans = list()

    for key, value in c.items():
        if value == count_max:
            ans.append(key)
    
    print(sorted(ans)[0])


if __name__ == "__main__":
    main()
