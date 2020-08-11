# -*- coding: utf-8 -*-


def main():
    from fractions import gcd

    n = int(input())
    a = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    lcm = 1 # 決め打ち
    ans = 0

    # 同じコードがPython3だとギリギリ通るが、PyPy3だとTLE
    for ai in a:
        lcm = lcm * ai // gcd(lcm, ai)

    for ai in a:
        # ここでmodを取らないとACできる
        ans += lcm // ai

    print(ans % mod)


if __name__ == '__main__':
    main()
