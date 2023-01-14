# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    summed = 0

    for ai in a:
        summed += ai

        if summed in b:
            summed = 0
    
    print(summed)
   

if __name__ == "__main__":
    main()
