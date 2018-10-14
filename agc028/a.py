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
    part_s = [s[0]]
    part_t = [t[0]]
    i = dm
    j = dn

    while i < n:
        part_s.append(s[i])
        i += dm

    while j < m:
        part_t.append(t[j])
        j += dn

    for si, ti in zip(part_s, part_t):
        if si != ti:
            print(-1)
            exit()

    print(size)


if __name__ == '__main__':
    main()
