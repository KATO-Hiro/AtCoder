# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s, t, x = map(int, input().split())
    
    if s > t:
        t += 24

        if s <= x < 24:
            pass
        else:
            x += 24
    
    if s <= x < t:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
