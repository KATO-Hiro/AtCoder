# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = list(input().rstrip())

    for si, sj in zip(s, s[1:]):
        if si == sj:
            print("No")
            exit()
    
    print("Yes")
    

if __name__ == "__main__":
    main()
