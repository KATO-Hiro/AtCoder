# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip() + "A"
    t = input().rstrip()
    count = 1

    for si, ti in zip(s, t):
        if si != ti:
            print(count)
            exit()
        
        count += 1
    

if __name__ == "__main__":
    main()
