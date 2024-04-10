# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    pos = [(1, 0)]
    x, y = 1, 0
    count = 0

    for _ in range(q):
        qi = list(input().rstrip().split())

        if qi[0] == "1":
            dir = qi[1]

            if dir == "L":
                x -= 1
            elif dir == "R":
                x += 1
            elif dir == "U":
                y += 1
            else:
                y -= 1

            count += 1

            pos.append((x, y))
        else:
            pi = int(qi[1])

            if count < pi:
                print(pi - count, 0)
            else:
                pos_x, pos_y = pos[-pi]
                print(pos_x, pos_y)


if __name__ == "__main__":
    main()
