# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    # <で区切ると>>>の部分だけが残る
    s = input().rstrip().split("<")
    ans = 0

    for si in s:
        m = len(si)
        ans += m * (m + 1) // 2

    print(ans)


if __name__ == "__main__":
    main()
