# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())
    s = input().rstrip()
    ans = "Yes"
    
    if s[a] != "-":
        ans = "No"
    elif not s[:a].isdigit() or not s[a + 1:].isdigit():
        ans = "No"
    
    print(ans)


if __name__ == "__main__":
    main()
