# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    l, n1, n2 = map(int, input().split())
    l1, l2 = 0, 0
    query = list()

    for _ in range(n1):
        vi, li = map(int, input().split())
        query.append((l1, vi, 1))
        l1 += li

    for _ in range(n2):
        vi, li = map(int, input().split())
        query.append((l2, vi, 2))
        l2 += li
    
    query.append((l, -1, -1))
    query = sorted(query, key=lambda x: x[0])
    x, y, prev, ans = -1, -1, 0, 0

    for li, vi, row in query:
        if x == y:
            ans += li - prev
        
        prev = li

        if row == 1:
            x = vi
        else:
            y = vi

    print(ans)


if __name__ == "__main__":
    main()
