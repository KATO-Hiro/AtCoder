# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n = int(input())
    # See:
    # https://atcoder.jp/contests/abc259/submissions/33090931
    d = defaultdict(lambda: (0, 0, False))  # index, e_max, is_unique
    
    for i in range(n):
        mi = int(input())

        for _ in range(mi):
            pi, ei  = map(int, input().split())
            e_max = d[pi][1]

            if e_max < ei:
                d[pi] = (i, ei, True)
            elif e_max == ei:
                d[pi] = (0, ei, False)
    
    candidate = set()

    for i, _, is_unique in d.values():
        if is_unique:
            candidate.add(i)

    ans = len(candidate)

    if ans < n:
        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
