# -*- coding: utf-8 -*-


def is_inside(ax, ay, bx, by, cx, cy, tx, ty):
    abXat = (bx - ax) * (ty - ay) - (by - ay) * (tx - ax)
    bcXbt = (cx - bx) * (ty - by) - (cy - by) * (tx - bx)
    caXct = (ax - cx) * (ty - cy) - (ay - cy) * (tx - cx)

    if (abXat > 0.0 and bcXbt > 0.0 and caXct > 0.0) or ( abXat < 0.0 and bcXbt < 0.0 and caXct < 0.0):
        return True
    elif (abXat * bcXbt * caXct == 0.0):
        return False
    
    return False


def is_concave(px, py):
    for i in range(4):
        if is_inside(px[i % 4], py[i % 4], px[(i + 1) % 4], py[(i + 1) % 4], px[(i + 2) % 4], py[(i + 2) % 4], px[(i + 3) % 4], py[(i + 3) % 4]):
            return True

    return False


def main():
    import sys

    input = sys.stdin.readline

    px = [0] * 4
    py = [0] * 4

    for i in range(4):
        xi, yi = map(int, input().split())
        px[i], py[i] = xi, yi
    
    if is_concave(px, py):
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
