# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(h)]
    t = [list(input().rstrip()) for _ in range(h)]

    # sとtの各行の"#"の個数が同じであればいいはず
    for si, ti in zip(s, t):
        if si.count("#") != ti.count("#"):
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
