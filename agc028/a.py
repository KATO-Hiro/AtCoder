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
    dn = size // n
    dm = size // m
    part_s = list()
    part_t = list()

    for i in range(0, n, dm):
        part_s.append(s[i])

    for i in range(0, m, dn):
        part_t.append(t[i])

    for si, ti in zip(part_s, part_t):
        if si != ti:
            print(-1)
            exit()

    print(size)


if __name__ == '__main__':
    main()
