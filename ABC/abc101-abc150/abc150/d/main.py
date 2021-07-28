# -*- coding: utf-8 -*-


def f(x):
    count = 0

    while x % 2 == 0:
        x //= 2
        count += 1

    return count


def lcm(a: int, b: int) -> int:
    '''Compute least common multiple of a and b.
    Args:
        a: Int of number (greater than 0).
        b: Int of number (greater than 0).
    Returns:
        least common multiple.
    Landau notation: O(log n)
    See:
    https://gist.github.com/endolith/114336/eff2dc13535f139d0d6a2db68597fad2826b53c3
    https://docs.python.org/3/library/sys.html#sys.version_info
    '''

    from math import gcd

    return a * b // gcd(a, b)


def main():
    from math import ceil
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0 for _ in range(n)]

    for index, ai in enumerate(a):
        if ai % 2 == 0:
            b[index] = ai // 2
        else:
            print(0)
            exit()

    t = f(b[0])

    for index, bi in enumerate(b[1:]):
        if f(bi) != t:
            print(0)
            exit()

        b[index] >>= t 

    l = b[0]

    for bi in b[1:]:
        l = lcm(l, bi)
    
    count = m // l
    print(ceil(count / 2))


if __name__ == "__main__":
    main()
