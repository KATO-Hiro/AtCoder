# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    q = int(input())
    d = deque([1])
    s = 1
    digit = 1
    mod = 998244353

    for _ in range(q):
        qi = list(map(int, input().split()))

        if qi[0] == 1:
            x = qi[1]
            s *= 10
            s += x
            s %= mod

            d.append(x)
            digit += 1
        elif qi[0] == 2:
            y = d.popleft()
            s -= y * pow(10, digit - 1, mod)
            s %= mod

            digit -= 1
        else:
            print(s % mod)


if __name__ == "__main__":
    main()
