# -*- coding: utf-8 -*-


def main():
    a, b = map(int, input().split())
    pins = ['x' for _ in range(10)]

    p = list(map(int, input().split()))

    for pi in p:
        pins[pi - 1] = '.'

    if b > 0:
        q = list(map(int, input().split()))

        for qi in q:
            pins[qi - 1] = 'o'

    print(' '.join(map(str, pins[6:])))
    print(' '.join(map(str, pins[3:6])))
    print(' '.join(map(str, pins[1:3])))
    print(' '.join(map(str, pins[0])))


if __name__ == '__main__':
    main()
