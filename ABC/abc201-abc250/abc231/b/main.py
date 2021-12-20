# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n = int(input())
    c = Counter()

    for _ in range(n):
        si = input().rstrip()
        
        if si not in c.keys():
            c[si] = 1
        else:
            c[si] += 1
    
    print(c.most_common()[0][0])



if __name__ == "__main__":
    main()
