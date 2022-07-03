# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    k = int(input())
    p, q = divmod(k, 60)
    h = str(21 + p)
    m = str(q)
    
    if len(m) == 1:
        m = '0' + m
    
    print(h + ":" + m)


if __name__ == "__main__":
    main()
