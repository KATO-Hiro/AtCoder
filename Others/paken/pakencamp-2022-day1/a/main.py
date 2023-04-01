# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, y = map(int, input().split())
    ans = 0

    if x != 0:
        ans += 1
    if y != 0:
        ans += 1

    print(ans)
    

if __name__ == "__main__":
    main()
