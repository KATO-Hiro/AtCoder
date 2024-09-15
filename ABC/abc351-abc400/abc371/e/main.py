# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import pairwise

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    s = [[] for _ in range(n)]

    # 加算の場合はΣの順番を並び替えても結果は変わらないため、Σの順番を入れ替える
    # 各aiについて、一致するなら1、そうでないなら0として、aiを1個以上含む区間の選び方の問題に帰着
    # 1個以上を直接数えるのは難しいので、余事象を取る
    for i, ai in enumerate(a):
        s[ai - 1].append(i)

    def nC2(n):
        return n * (n - 1) // 2

    ans = 0

    # 一見するとO(N ** 2)に見えるが、sは全体でN個なのでO(N)
    for x in range(n):
        excluded = 0

        # 端部の処理
        for first, second in pairwise([-1] + s[x] + [n]):
            excluded += nC2(second - first - 1 + 1)

        ans += nC2(n + 1) - excluded

    print(ans)


if __name__ == "__main__":
    main()
