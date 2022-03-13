# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x = map(int, input().split())
    s = input().rstrip()
    x = list(bin(x)[2:])

    for si in s:
        if si == "U":
            x.pop()
        elif si == "L":
            x.append("0")
        else:
            x.append("1")
    
    print(int(''.join(x), 2))


if __name__ == "__main__":
    main()
