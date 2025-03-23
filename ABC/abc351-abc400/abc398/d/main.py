# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, r, c = map(int, input().split())
    s = input().rstrip()
    y, x = 0, 0
    smokes = set()
    smokes.add((0, 0))
    ans = list()

    # 煙の視点から、焚き火と人が指定される方向の逆向きに移動すると言い換え
    for si in s:
        if si == "N":
            y += 1
        elif si == "S":
            y -= 1
        elif si == "W":
            x += 1
        elif si == "E":
            x -= 1

        smokes.add((y, x))

        if (y + r, x + c) in smokes:
            ans += "1"
        else:
            ans += "0"

    print("".join(ans))


if __name__ == "__main__":
    main()
