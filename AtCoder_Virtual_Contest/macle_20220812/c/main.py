# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    words = set(["dream", "dreamer", "erase", "eraser"])
    s = input().rstrip()[::-1]
    u = ""

    for si in s:
        u = si + u
        size = len(u)

        if 5 <= size <= 7:
            if u in words:
                u = ""

        if size >= 8:
            print("NO")
            exit()
    
    print("YES")


if __name__ == "__main__":
    main()
