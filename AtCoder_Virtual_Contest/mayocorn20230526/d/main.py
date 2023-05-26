# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    q = int(input())
    d = deque([1])
    mod = 998244353
    inv = pow(10, mod - 2, mod)  # 1 / p
    ans = 1

    for _ in range(q):
        qi = list(map(int, input().split()))

        if qi[0] == 1:
            x = qi[1]

            ans *= 10
            ans %= mod
            ans += x
            ans %= mod

            d.append(x)
        elif qi[0] == 2:
            di = d.popleft()
            size = len(d)

            ans -= di * pow(10, size, mod) % mod
            ans %= mod
        else:
            print(ans)


if __name__ == "__main__":
    main()
