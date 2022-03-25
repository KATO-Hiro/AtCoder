# -*- coding: utf-8 -*-


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
    from math import gcd
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    l = a[0]
    f = 0

    for ai in a[1:]:
        l = lcm(l, ai)
    
    for ai in a:
        f += l // ai
    
    print(l / f)


if __name__ == "__main__":
    main()
