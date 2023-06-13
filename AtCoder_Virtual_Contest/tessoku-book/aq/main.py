# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, l = map(int, input().split())
    to_east, to_west = [l], [0]

    # 2人が同じ位置に来たら移動方向を変える = 2人ともそのままの方向へ歩き続ける、とみなす
    for _ in range(n):
        ai, bi = input().rstrip().split()
        ai = int(ai)

        if bi == "E":
            to_east.append(ai)
        else:
            to_west.append(ai)

    print(max(l - min(to_east), max(to_west)))


if __name__ == "__main__":
    main()
