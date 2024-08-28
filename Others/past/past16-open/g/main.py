# -*- coding: utf-8 -*-


def main():
    import sys

    sys.setrecursionlimit(10**7)

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))

    # 三角形の判定
    def f(x, y, z):
        return (x + y > z) and (y + z > x) and (z + x > y)

    # 組み合わせを全探索
    def dfs(a):
        size = len(a)

        if size == 0:
            return 1

        ans = 0

        # 3つの要素を0番目、j番目、k番目として取り出す
        for j in range(1, size):
            for k in range(j + 1, size):
                if f(a[0], a[j], a[k]):
                    # 0番目、j番目、k番目を除外して再帰的に処理
                    ans += dfs(a[1:j] + a[j + 1 : k] + a[k + 1 :])

        return ans

    print(dfs(a))


if __name__ == "__main__":
    main()
