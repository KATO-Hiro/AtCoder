# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c, d, e, f, x = map(int, input().split())

    unit_t = a + c
    unit_a = d + f
    p1, q1 = divmod(x, unit_t)
    p2, q2 = divmod(x, unit_a)

    dist_t = p1 * (a * b) + min(q1, a) * b
    dist_a = p2 * (d * e) + min(q2, d) * e

    if dist_t > dist_a:
        print("Takahashi")
    elif dist_t < dist_a:
        print("Aoki")
    else:
        print("Draw")


if __name__ == "__main__":
    main()
