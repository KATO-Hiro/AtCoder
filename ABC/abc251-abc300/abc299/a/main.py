# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    one = list()
    two = list()

    for i, si in enumerate(s):
        if si == "|":
            two.append(i)
        elif si == "*":
            one.append(i)
    
    if two[0] < one[0] < two[1]:
        print("in")
    else:
        print("out")
    

if __name__ == "__main__":
    main()
