# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    sx, sy = map(int, input().split())
    tx, ty = map(int, input().split())

    # See:
    # https://atcoder.jp/contests/abc359/editorial/10278
    # タイルの右側にある場合は、左側に寄せておく(同一タイルでは移動コストが0)
    sx -= (sy - sx) % 2
    tx -= (ty - tx) % 2

    # 平行移動で片方を原点に
    tx -= sx
    ty -= sy

    # 対称性を利用して、tx, tyともに正の場合のみを考える
    tx, ty = abs(tx), abs(ty)

    # ty >= txのときは、y回移動するのが最適
    # ty < txのときは、さらに(tx - ty) // 2回移動が必要
    ans = ty + max(0, tx - ty) // 2
    print(ans)


if __name__ == "__main__":
    main()
