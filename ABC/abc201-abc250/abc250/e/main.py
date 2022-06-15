# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    d = defaultdict(int)
    count_a, count_b = [0] * n, [0] * n

    for i, ai in enumerate(a):
        if ai not in d.keys():
            d[ai] = len(d.keys()) + 1
        
        count_a[i] = len(d.keys())

    inf = 10 ** 18
    max_value = 0
    max_values = [0] * n
    set_b = set()
    
    for i, bi in enumerate(b):
        set_b.add(bi)

        if bi not in d.keys():
            max_value = inf
        
        max_value = max(max_value, d[bi])
        max_values[i] = max_value

        count_b[i] = len(set_b)

    q = int(input())

    for i in range(q):
        xi, yi = map(int, input().split())
        xi -= 1
        yi -= 1

        if (count_a[xi] == count_b[yi]) and (max_values[yi] == count_b[yi]):
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
