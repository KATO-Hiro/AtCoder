# -*- coding: utf-8 -*-


def main():
    from itertools import product
    from collections import Counter
    import sys

    input = sys.stdin.readline
    
    n, k = map(int, input().split())
    s = [input().rstrip() for _ in range(n)]
    ans = 0

    for pattern in product([0, 1], repeat=n):
        t = list()
        
        for i, pi in enumerate(pattern):
            if pi == 1:
                for si in s[i]:
                    t.append(si)

        c = Counter(t)
        count = 0

        for value in c.values():
            if value == k:
                count += 1
    
        ans = max(ans, count)

    print(ans)


if __name__ == "__main__":
    main()
