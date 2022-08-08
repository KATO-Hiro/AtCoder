# -*- coding: utf-8 -*-


def main():
    from itertools import permutations
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    ans = list()

    for pattern in permutations(range(1, m + 1), n):
        ok = True

        for f, s in zip(pattern, pattern[1:]):
            if f > s:
                ok = False
                break
        
        if ok:
            ans.append(pattern)
    
    for a in sorted(ans):
        print(*a)


if __name__ == "__main__":
    main()
