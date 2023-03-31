# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline


    n = int(input())
    w = set(input().rstrip().split())
    s = set(["and", "not", "that", "the", "you"])
    common = w & s

    if len(common) > 0:
        print("Yes")
    else:
        print("No")
    

if __name__ == "__main__":
    main()
