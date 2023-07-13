# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    q = int(input())
    d = deque([1])
    ans = 1
    mod = 998244353

    for _ in range(q):
        qi = list(map(int, input().split()))

        if qi[0] == 1:
            xi = qi[1]

            d.append(xi)
            ans *= 10
            ans += xi
            ans %= mod
        elif qi[0] == 2:
            digit = len(d) - 1
            di = d.popleft()

            ans -= di * pow(10, digit, mod)
            ans %= mod
        else:
            print(ans)


if __name__ == "__main__":
    main()
