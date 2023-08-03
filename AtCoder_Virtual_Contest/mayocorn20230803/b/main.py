# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in range(n)]
    ans = 0

    # 3頂点から面積を求める
    # See:
    # https://mathwords.net/x1y2hikux2y1
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                (xi, yi), (xj, yj), (xk, yk) = xy[i], xy[j], xy[k]

                # 面積を求める1/2は省略
                if (xj - xi) * (yk - yi) != (xk - xi) * (yj - yi):
                    ans += 1

    print(ans)


if __name__ == "__main__":
    main()
