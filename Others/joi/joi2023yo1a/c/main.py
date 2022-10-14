# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    x = 1
    ans = 0

    for si in s:
        if si == "L":
            x = max(1, x - 1)
        else:
            x = min(3, x + 1)

        if x == 3:
            ans += 1
    
    print(ans)


if __name__ == "__main__":
    main()
