# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = list(map(int, input().split()))
    ans = [s[0]]

    for si, ti in zip(s, s[1:]):
        ans.append(ti - si)
    
    print(*ans)
    

if __name__ == "__main__":
    main()
