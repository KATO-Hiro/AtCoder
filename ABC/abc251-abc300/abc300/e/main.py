# -*- coding: utf-8 -*-


def main():
    from functools import lru_cache

    import sys
    sys.setrecursionlimit(10 ** 8)

    input = sys.stdin.readline

    n = int(input())
    mod = 998244353
    inv = pow(5, mod - 2, mod)  # 1 / p

    # See:
    # https://atcoder.jp/contests/abc300/submissions/40930557
    # 2、3、5で何回割り切れるか?
    two, three, five = 0, 0, 0

    while n % 2 == 0:
        n //= 2
        two += 1

    while n % 3 == 0:
        n //= 3
        three += 1
    
    while n % 5 == 0:
        n //= 5 
        five += 1
    
    if n != 1:
        print(0)
    else:
        # メモ化再帰
        @lru_cache(maxsize=10 ** 6)
        def f(two, three, five):
            if (two, three, five) == (0, 0, 0):
                return 1
            
            ans = 0

            if two >= 1:
                ans += f(two - 1, three, five)
            if three >= 1:
                ans += f(two, three - 1, five)
            if two >= 2:
                ans += f(two - 2, three, five)
            if five >= 1:
                ans += f(two, three, five - 1)
            if two >= 1 and three >= 1:
                ans += f(two - 1, three - 1, five)

            return ans * inv % mod
        
        print(f(two, three, five))


if __name__ == "__main__":
    main()
