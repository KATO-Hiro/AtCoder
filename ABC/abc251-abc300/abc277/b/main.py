# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    first = ["H", "D", "C", "S"]
    second = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
    s = set()

    for _ in range(n):
        si = input().rstrip()

        if si[0] not in first:
            print("No")
            exit()

        if si[1] not in second:
            print("No")
            exit()
        
        s.add(si)
    
    if len(s) == n:
        print("Yes")
    else:
        print("No")
    

if __name__ == "__main__":
    main()
