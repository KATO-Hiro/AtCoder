# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline


    n = int(input())
    w = list(input().rstrip().split())
    s = ["and", "not", "that", "the", "you"]

    for wi in w:
        if wi in s:
            print("Yes")
            exit()
    
    print("No")
    

if __name__ == "__main__":
    main()
