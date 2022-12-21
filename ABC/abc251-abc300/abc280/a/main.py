# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    ans = 0
    
    for _ in range(h):
        si = input().rstrip()
        ans += si.count("#")

    print(ans)
    

if __name__ == "__main__":
    main()
