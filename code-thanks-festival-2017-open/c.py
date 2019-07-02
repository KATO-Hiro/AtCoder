# -*- coding: utf-8 -*-


def main():
    from heapq import heappop
    from heapq import heappush

    n, k = map(int, input().split())
    b = [0 for _ in range(n)]
    hq = list()
    ans = 0

    for i in range(n):
        ai, bi = map(int, input().split())
        b[i] = bi
        heappush(hq, (ai, i))

    for i in range(k):
        time, index = heappop(hq)
        ans += time

        heappush(hq, (time + b[index], index))

    print(ans)


if __name__ == '__main__':
    main()
