# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    from bisect import bisect_left
    import sys

    input = sys.stdin.readline

    l, n1, n2 = map(int, input().split())
    v1, l1, v2, l2 = [0] * n1, [0] * n1, [0] * n2, [0] * n2

    for i in range(n1):
        v1i, l1i = map(int, input().split())
        v1[i], l1[i] = v1i, l1i

    for i in range(n2):
        v2i, l2i = map(int, input().split())
        v2[i], l2[i] = v2i, l2i
    
    l1_acc = list(accumulate(l1))
    l2_acc = list(accumulate(l2))
    pos = sorted(set([*l1_acc, *l2_acc]))
    prev, ans = 0, 0

    for p in pos:
        i1 = bisect_left(l1_acc, p)
        i2 = bisect_left(l2_acc, p)

        if v1[i1] == v2[i2]:
            ans += p - prev
        
        prev = p

    print(ans)


if __name__ == "__main__":
    main()
