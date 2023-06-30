# -*- coding: utf-8 -*-


def division_in_mod(a, b, mod=998244353) -> int:
    inv = pow(b, mod - 2, mod)  # 1 / b

    return (a * inv) % mod


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    mod = 10**9 + 7

    # (a[i] * x) % mod = p
    # modが素数の世界では、1 / ai = 逆元を取る
    ans = 0

    # 片方を決めうちして、もう片方を高速に求める
    for i, ai in enumerate(a, 1):
        ai %= mod

        # コーナーケース: 0除算を回避
        if ai == 0:
            if p == 0:
                # 直前までの要素なら、どれでも選べる
                ans += i - 1
        else:
            x = division_in_mod(p, ai, mod)
            ans += d[x]

        d[ai] += 1

    print(ans)


if __name__ == "__main__":
    main()
