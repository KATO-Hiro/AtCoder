# -*- coding: utf-8 -*-


def main():
    n = int(input())
    ts, xs, ys = [0], [0], [0]

    for i in range(n):
        ti, xi, yi = map(int, input().split())
        ts.append(ti)
        xs.append(xi)
        ys.append(yi)

    for j in range(n):
        dt = ts[j + 1] - ts[j]
        dxy = (xs[j + 1] - xs[j]) + (ys[j + 1] - ys[j])

        if (-dt <= dxy <= dt) and (dt % 2 == dxy % 2):
            pass
        else:
            print('No')
            exit()

    print('Yes')


if __name__ == '__main__':
    main()
