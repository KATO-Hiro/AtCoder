# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k, m = map(int, input().split())
    mod = 998244353

    # 組み合わせm ** (k ** n)通り
    # modの世界で考える
    # フェルマーの小定理を適用できる a ** (p - 1) ≡ 1 (mod p)
    # m ** p ≡ m ** (x % (p - 1))。ただし、m != 0
    r = pow(k, n, mod - 1)
    ans = pow(m, r, mod)

    if m % mod == 0:
        ans = 0

    print(ans)


if __name__ == "__main__":
    main()
