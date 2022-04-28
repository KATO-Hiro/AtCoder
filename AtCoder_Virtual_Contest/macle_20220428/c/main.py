# -*- coding: utf-8 -*-


def main():
    from itertools import product
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    n = len(s)
    ans = 0

    for pattern in product(["+", ""], repeat=n-1):
        t = s[0]

        for pi, ti in zip(pattern, s[1:]):
            t += pi + ti
        
        ans += eval(t)

    print(ans)


if __name__ == "__main__":
    main()
