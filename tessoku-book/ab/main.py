# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    mod = 10 ** 4
    t = 0

    for _ in range(n):
        ti, ai = input().rstrip().split(" ")
        ai = int(ai)

        if ti == "+":
            t += ai
        elif ti == "-":
            t -= ai
        else:
            t *= ai
        
        t %= mod
    
        print(t)
    

if __name__ == "__main__":
    main()
