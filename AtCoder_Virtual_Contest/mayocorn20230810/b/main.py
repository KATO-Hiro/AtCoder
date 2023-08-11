# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    t = s.split("-")
    ans = -1

    if s.count("o") == 0 or s.count("-") == 0:
        print(ans)
        exit()

    # print(s)

    for ti in t:
        ans = max(ans, len(ti))

    print(ans)


if __name__ == "__main__":
    main()
