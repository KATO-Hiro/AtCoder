# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    s = input().rstrip()
    count = 1
    ans = ""

    for si in s:
        if si == "o" and count <= k:
            ans += si
            count += 1
        else:
            ans += "x"
    
    print(ans)
    

if __name__ == "__main__":
    main()
