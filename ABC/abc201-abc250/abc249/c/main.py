# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    from itertools import product
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    s = [input().rstrip() for _ in range(n)]
    patterns = product([0, 1], repeat=n)
    ans = 0

    for pattern in patterns:
        t = list()
        count = 0

        for i, p in enumerate(pattern):
            if p == 1:
                for si in s[i]:
                    t.append(si)
        
        c = Counter(t)

        for value in c.values():
            if value == k:
                count += 1

        ans = max(ans, count)
    
    print(ans)



if __name__ == "__main__":
    main()
