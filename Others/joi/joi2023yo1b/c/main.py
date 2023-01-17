# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()

    if s[:n // 2] == s[n // 2:]:
        print("Yes")
    else:
        print("No")
   

if __name__ == "__main__":
    main()
