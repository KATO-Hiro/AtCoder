# -*- coding: utf-8 -*-


def main():
    from itertools import product
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    n = len(s)
    patterns = product(["+", ""], repeat=n -1)
    total = 0

    for pattern in patterns:
        t = s[0]
        
        for si, pi in zip(s[1:], pattern):
            t += pi + si
        
        total += eval(t)
    
    print(total)


if __name__ == "__main__":
    main()
