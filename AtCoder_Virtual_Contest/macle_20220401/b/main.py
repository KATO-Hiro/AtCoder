# -*- coding: utf-8 -*-


def main():
    from math import ceil
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())

    if m == 0:
        print(1)
        exit()
    elif m == n:
        print(0)
        exit()

    a = sorted(list(map(int, input().split())))

    if 1 not in a:
        a = [0] + a
    if n not in a:
        a += [n + 1]
    
    diff = float('inf')
    
    for first, second in zip(a, a[1:]):
        candidate = second - first - 1

        if candidate == 0:
            continue

        diff = min(diff, candidate)
    
    ans = 0

    for first, second in zip(a, a[1:]):
        ans += ceil((second - first - 1) / diff)
    
    print(ans)


if __name__ == "__main__":
    main()
