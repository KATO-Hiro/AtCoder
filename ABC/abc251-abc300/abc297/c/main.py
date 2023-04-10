# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = [input().rstrip() for _ in range(h)]

    for si in s:
        print(si.replace("TT", "PC"))
    

if __name__ == "__main__":
    main()
