# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a, b, c, d = map(int, input().split())
    # 浮動小数は、誤差を回避するため文字列として読み込む
    x = int(input().rstrip().replace(".", ""))

    ng, ok = -1, 10**18

    while ok - ng > 1:
        wj = (ok + ng) // 2
        rank = (a + wj) + 2 * b + 3 * c + 4 * d
        rank *= 10**3  # xを浮動小数から整数にしたため

        if rank <= x * (n + wj):
            ok = wj
        else:
            ng = wj

    print(ok)


if __name__ == "__main__":
    main()
