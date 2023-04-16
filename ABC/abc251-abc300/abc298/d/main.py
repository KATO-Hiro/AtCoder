# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    q = int(input())
    d = deque(["1"])
    mod = 998244353
    digit_count = 1
    ans = 1
    
    for _ in range(q):
        qi = list(map(int, input().split()))

        if qi[0] == 1:
            x = qi[1]

            d.append(str(x))

            ans *= 10
            ans += x
            ans %= mod

            digit_count += 1
        elif qi[0] == 2:
            value = int(d.popleft())

            ans -= value * pow(10, digit_count - 1, mod)
            ans %= mod

            digit_count -= 1
        else:
            print(ans % mod)
    

if __name__ == "__main__":
    main()
