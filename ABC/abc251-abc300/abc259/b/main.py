# -*- coding: utf-8 -*-


def main():
    from math import cos, sin, radians
    import sys

    input = sys.stdin.readline

    a, b, d = map(int, input().split())

    # See:
    # https://note.nkmk.me/python-complex/
    # https://science-log.com/%E6%95%B0%E5%AD%A6/%E5%9B%B3%E5%BD%A2%E3%81%AE%E5%9B%9E%E8%BB%A2%E3%81%AB%E3%81%AF%E8%A4%87%E7%B4%A0%E6%95%B0%E3%81%AE%E7%A9%8D%E3%82%92%E4%BD%BF%E3%81%8A%E3%81%86%EF%BC%81/
    ans = complex(a, b) * complex(cos(radians(d)), sin(radians(d)))
    print(ans.real, ans.imag)


if __name__ == "__main__":
    main()
