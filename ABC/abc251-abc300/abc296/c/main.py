# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    s = set(a)
    
    for ai in a:
        if (ai + x) in s:
            print("Yes")
            exit()
    
    print("No")
    

if __name__ == "__main__":
    main()
