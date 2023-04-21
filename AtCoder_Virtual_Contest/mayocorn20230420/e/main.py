# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, d = map(int, input().split())
    mod = 998244353

    # 完全二分木
    # 再帰的な構造を漸化式で表現
    # 木の高さhおよび距離dと置くと、f(n, d) = f(n - 1, d) * 2 + 根を通るパスg(n, d)
    # g(n, d) = g(n - 1, d) + 葉を通るパス
    two = [0] * (n + 1)
    two[0] = 1

    for i in range(1, n + 1):
        two[i] = two[i - 1] * 2
        two[i] %= mod

    g = [0] * (n + 1)

    for i in range(1, n + 1):
        left = i - 1
        right = d - left
        leaf_count = 0

        if 0 <= right <= i - 1:
            leaf_count = two[max(0, left - 1)] * two[max(0, right - 1)]
            leaf_count %= mod

            if left != right:
                leaf_count *= 2
                leaf_count %= mod
        
        g[i] = g[i - 1] + leaf_count
        g[i] %= mod

    f = [0] * (n + 1)
    
    for i in range(1, n + 1):
        f[i] = f[i - 1] * 2 + g[i]
        f[i] %= mod

    print((f[n] * 2) % mod)


if __name__ == "__main__":
    main()
