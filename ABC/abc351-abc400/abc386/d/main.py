# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    yxc = list()

    for _ in range(m):
        yi, xi, ci = input().rstrip().split()
        yi = int(yi)
        xi = int(xi)
        yxc.append((yi, xi, ci))

    yxc.sort()

    # ci = "B"、cj = "W"、yi <= yj のとき、xi <= xj なら 条件を満たす
    # ソートで、yi <= yjは常に満たされているので、xのみ比較すればよい
    # ci = "W"、cj = "B" のとき、xi <= xj なら "No"
    x_min = 1 << 30

    for _, xi, ci in yxc:
        if ci == "W":
            x_min = min(x_min, xi)
        else:
            if xi >= x_min:
                print("No")
                exit()

    print("Yes")


if __name__ == "__main__":
    main()
