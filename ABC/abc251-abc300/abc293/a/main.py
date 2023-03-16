# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    odd = s[::2]
    even = s[1::2]
    ans = ""

    for o, e in zip(odd, even):
        ans += e
        ans += o
    
    print(ans)
    

if __name__ == "__main__":
    main()
