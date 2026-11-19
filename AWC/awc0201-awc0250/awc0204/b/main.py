# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    ans = -1

    for i, si in enumerate(s, 1):
        if si == "o":
            continue

        ans = i
        break

    print(ans)


if __name__ == "__main__":
    main()
