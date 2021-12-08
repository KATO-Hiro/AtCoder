# -*- coding: utf-8 -*-


def main():
    from heapq import heappush, heappop, heapify
    import sys

    input = sys.stdin.readline

    n, d = map(int, input().split())
    l = list()
    r = list()
    used = [False] * n
    count = 0

    for i in range(n):
        li, ri = map(int, input().split())
        l.append((li, i))
        r.append((ri, i))
    
    heapify(l)
    heapify(r)

    while r:
        ri, i = heappop(r)

        if used[i]:
            continue

        count += 1
        used[i] = True

        while l:
            li, j = heappop(l)

            if used[j]:
                continue

            if li <= ri + d - 1:
                used[j] = True
            else:
                heappush(l, (li, j))
                break

    print(count)


if __name__ == "__main__":
    main()
