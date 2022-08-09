# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline
    
    s1, s2, s3 = map(str, input().split())
    print(s1[0].upper() + s2[0].upper() + s3[0].upper())


if __name__ == "__main__":
    main()
