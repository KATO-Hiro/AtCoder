# -*- coding: utf-8 -*-


def main():
    from itertools import product
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    n = len(s)
    patterns = product(["", "+"], repeat=n-1)
    ans = 0

    for pattern in patterns:
        value = s[0]

        for i, p in enumerate(pattern, 1):
            value += p + s[i]
    
        ans += eval(value)

    print(ans)


if __name__ == "__main__":
    main()
