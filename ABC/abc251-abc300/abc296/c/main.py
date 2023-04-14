# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n, x = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    c = Counter(a)
    
    for ai in a:
        if (ai - x) in c.keys():
            print("Yes")
            exit()
    
    print("No")
    

if __name__ == "__main__":
    main()
