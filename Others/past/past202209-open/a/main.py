# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, y, z = map(int, input().split())
    print(max(x + z, y))
    

if __name__ == "__main__":
    main()
