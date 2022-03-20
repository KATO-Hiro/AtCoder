# -*- coding: utf-8 -*-


def main():
    from math import ceil
    import sys

    input = sys.stdin.readline
    
    n, m = map(int, input().split())

    if m == 0:
        print(1)
        exit()

    if n == m:
        print(0)
        exit()
    
    a = sorted(list(map(int, input().split())))
    
    if 1 not in a:
        a = [0] + a
    
    if n not in a:
        a = a + [n + 1]

    dist = list()
    
    for first, second in zip(a, a[1:]):
        diff = second - first - 1

        if diff != 0:
            dist.append(diff)
    
    ans = 0
    k = min(dist)

    for d in dist:
        ans += ceil(d / k)

    print(ans)


if __name__ == "__main__":
    main()
