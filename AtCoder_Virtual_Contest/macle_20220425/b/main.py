# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x = int(input())
    p, q = divmod(x, 11)
    p *= 2

    if 1 <= q <= 6:
        p += 1
    elif q >= 7:
        p += 2
    
    print(p)
    

if __name__ == "__main__":
    main()
