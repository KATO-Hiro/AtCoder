# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = list(input().rstrip())
    t = list()
    u = ""

    for i, si in enumerate(s, 1):
        if si == "B":
            t.append(i)
        elif si == "R" or si == "K":
            u += si
    
    if (t[0] % 2 != t[1] % 2) and u == "RKR":
        print("Yes")
    else:
        print("No")
    

if __name__ == "__main__":
    main()
