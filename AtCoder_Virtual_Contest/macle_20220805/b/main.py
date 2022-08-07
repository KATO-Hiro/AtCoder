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

    from sys import version_info

    if version_info.major == 3 and version_info.minor >= 5:
        from math import gcd
    else:
        from fractions import gcd

    return a * b // gcd(a, b)


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = 1

    for i in range(n):
        ti = int(input())
        ans = lcm(ans, ti)
    
    print(ans)


if __name__ == "__main__":
    main()
