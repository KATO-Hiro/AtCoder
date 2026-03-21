# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [ai % k for ai in a]
    b.sort()
    d = deque(b)
    inf = 10**18
    ans = inf

    for _ in range(n):
        candidate = d[-1] - d[0]
        ans = min(ans, candidate)

        di = d.popleft()
        d.append(di + k)

    print(ans)


if __name__ == "__main__":
    main()
