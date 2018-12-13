# -*- coding: utf-8 -*-


def main():
    from math import hypot

    txa, tya, txb, tyb, large_t, v = map(int, input().split())
    n = int(input())
    ans = 'NO'

    for i in range(n):
        xi, yi = map(int, input().split())

        dist1 = hypot(txa - xi, tya - yi)
        dist2 = hypot(xi - txb, yi - tyb)
        dist = dist1 + dist2

        if dist <= large_t * v:
            print('YES')
            exit()

    print(ans)


if __name__ == '__main__':
    main()
