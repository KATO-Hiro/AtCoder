# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n, k = map(int, input().split())

    if n < k:
        print(1)
    else:
        d = deque([1] * k + [k])
        mod = 10**9

        for i in range(k, n):
            value = d[-1] * 2 - d[0]
            value %= mod
            d.append(value)
            d.popleft()

        ans = d[-1]
        print(ans)


if __name__ == "__main__":
    main()
