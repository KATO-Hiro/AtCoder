# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = [input().rstrip() for _ in range(10)]
    ab = list()
    cd = list()

    for i, si in enumerate(s, 1):
        if si.count("#") >= 1:
            ab.append(i)
    
    for j in range(10):
        count = 0
        
        for i in range(10):
            if s[i][j] == "#":
                count += 1
    
        if count >= 1:
            cd.append(j + 1)
    
    print(min(ab), max(ab))
    print(min(cd), max(cd))


if __name__ == "__main__":
    main()
