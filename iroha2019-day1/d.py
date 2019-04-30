# -*- coding: utf-8 -*-


def main():
    n, x, y = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    t = x + sum(a[::2])
    a = y + sum(a[1::2])

    if t > a:
        print('Takahashi')
    elif t < a:
        print('Aoki')
    else:
        print('Draw')


if __name__ == '__main__':
    main()
