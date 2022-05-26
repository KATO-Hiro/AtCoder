# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c, d, e, f, x = map(int, input().split())
    dist_t, dist_a = 0, 0

    p1, q1 = divmod(x, a + c)
    dist_t = a * p1 * b
    dist_t += min(q1, a) * b

    p2, q2 = divmod(x, d + f)
    dist_a = d * p2 * e
    dist_a += min(q2, d) * e
    
    if dist_t > dist_a:
        print('Takahashi')
    elif dist_t < dist_a:
        print('Aoki')
    else:
        print('Draw')


if __name__ == "__main__":
    main()
