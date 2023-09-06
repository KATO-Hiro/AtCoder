# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    xy1 = [tuple(map(int, input().split())) for _ in range(n)]
    m = int(input())
    xy2 = [tuple(map(int, input().split())) for _ in range(m)]
    xy2 = set(xy2)

    # 最も外側のループは事実上1ペアしか使っていないので、xy1の1点だけを利用すれば良い
    # for x1, y1 in xy1:
    for x2, y2 in xy2:
        x1, y1 = xy1[0]
        dx, dy = x2 - x1, y2 - y1
        ok = True

        for x3, y3 in xy1:
            nx, ny = x3 + dx, y3 + dy

            if (nx, ny) not in xy2:
                ok = False
                break

        if ok:
            print(dx, dy)
            exit()


if __name__ == "__main__":
    main()
