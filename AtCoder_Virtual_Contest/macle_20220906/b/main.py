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


def f(i, c, d):
    ans = i

    ans -= i // c
    ans -= i // d
    ans += i // lcm(c, d)

    return ans


def main():
    import sys

    input = sys.stdin.readline

    a, b, c, d = map(int, input().split())
    a -= 1
    print(f(b, c, d) - f(a, c, d))


if __name__ == "__main__":
    main()
