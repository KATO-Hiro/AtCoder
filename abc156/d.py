# -*- coding: utf-8 -*-


def main():
    n, a, b = map(int, input().split())
    value_max = 2 * (10 ** 5)
    com = [0 for _ in range(value_max + 1)]
    com[1] = n
    mod = 10 ** 9 + 7
    mod_inverse = [pow(i, mod - 2, mod) for i in range(1, value_max + 1)]
    ans = pow(2, n, mod)

    # KeyInsight:
    # 全体 - 条件を満たす場合
    # modの世界では割り算の代わりに逆元を使う
    # See:
    # https://www.youtube.com/watch?v=lzAMKPMLdtU&feature=youtu.be
    for i in range(2, min(n, value_max) + 1):
        if (n - i + 1) == 0:
            break

        com[i] = com[i - 1] * (n - i + 1)
        com[i] *= mod_inverse[i - 1]
        com[i] %= mod

    diff = (com[a] + com[b] + 1) % mod
    print((ans - diff) % mod)


if __name__ == '__main__':
    main()
