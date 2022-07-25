# -*- coding: utf-8 -*-


def main():
    from itertools import product
    import sys

    input = sys.stdin.readline

    s = list(input().rstrip())
    n = len(s)
    ans = float("inf")

    for pattern in product([0, 1], repeat=n):
        if sum(pattern) == 0:
            continue
    
        number = ''
        count = 0

        for si, pi in zip(s, pattern):
            if pi == 0:
                count += 1
            else:
                number += si
        
        if int(number) % 3 == 0:
            ans = min(ans, count)
    
    if ans == float("inf"):
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    main()
