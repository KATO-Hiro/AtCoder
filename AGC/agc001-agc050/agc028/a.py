# -*- coding: utf-8 -*-


def lcm(x: int, y: int):
    '''
    See:
    https://note.nkmk.me/python-gcd-lcm/
    '''
    from fractions import gcd
    return (x * y) // gcd(x, y)


def main():
    n, m = map(int, input().split())
    s = input()
    t = input()
    size = lcm(n, m)
    part_s = [s[i] for i in range(0, n, size // m)]
    part_t = [t[j] for j in range(0, m, size // n)]

    for si, ti in zip(part_s, part_t):
        if si != ti:
            print(-1)
            exit()

    print(size)


if __name__ == '__main__':
    main()
