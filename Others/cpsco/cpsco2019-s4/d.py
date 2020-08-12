# -*- coding: utf-8 -*-


def main():
    from heapq import heappush, heappop, heapify

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a_count = list()
    b = list()
    count = 1
    pre = a[0]

    for i in range(1, n):
        cur = a[i]

        if cur == pre:
            count += 1
        else:
            a_count.append(count)
            count = 1
            pre = cur

    if count >= 1:
        a_count.append(count)

    for element in a_count:
        heappush(b, -element)

    for i in range(k):
        c = -heappop(b)
        d = c // 2
        e = c - d
        heappush(b, -d)
        heappush(b, -e)
        print(c, d, e)

    print(b)

if __name__ == '__main__':
    main()
