# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s, t = input().rstrip().split(".")
    ans = int(s)
    
    if int(t[0]) >= 5:
        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
