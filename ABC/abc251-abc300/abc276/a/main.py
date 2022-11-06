# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    ans = -1

    for i, si in enumerate(s, 1):
        if si == "a":
            ans = i

    print(ans)
    

if __name__ == "__main__":
    main()
