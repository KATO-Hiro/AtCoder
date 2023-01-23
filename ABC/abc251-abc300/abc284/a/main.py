# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = list()
    
    for _ in range(n):
        si = input().rstrip()
        ans.append(si)

    for si in ans[::-1]:
        print(si)
    

if __name__ == "__main__":
    main()
