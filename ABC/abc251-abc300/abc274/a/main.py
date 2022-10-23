# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline
    
    a, b = map(int, input().split())
    c = list(str(b / a) + "0000")

    if int(c[5]) >= 5:
        c[4] = str(int(c[4]) + 1)
    
    print(''.join(c)[:5])


if __name__ == "__main__":
    main()
