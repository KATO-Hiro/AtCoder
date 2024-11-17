# -*- coding: utf-8 -*-


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    s = input().rstrip()
    n = len(s)
    q = int(input())
    k = list(map(int, input().split()))
    ans = list()

    # 操作回数(level)は実質60回まで
    # クエリのki番目がlevel - 1回目で、前半もしくは後半のどちらに含まれるかを再帰的に判断
    def f(pos, level):
        if level == 0:
            return s[pos - 1]  # 0-indexed

        size = n * (1 << (level - 1))

        if pos <= size:
            return f(pos, level - 1)

        # アスキーコードを利用して、'a' <=> 'A'の変換を行う
        return chr(ord(f(pos - size, level - 1)) ^ 32)

    for ki in k:
        ans.append(f(ki, 60))

    print(*ans)


if __name__ == "__main__":
    main()
