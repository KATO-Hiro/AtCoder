# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = list(input().rstrip())
    ans = 0

    for i in range(1, n - 1):
        x, y = set(s[:i]), set(s[i:])
        ans = max(ans, len(x & y))
    
    print(ans)


if __name__ == "__main__":
    main()
