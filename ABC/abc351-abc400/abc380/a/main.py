# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    ans = "Yes"

    for i in range(1, 4):
        if s.count(str(i)) != i:
            ans = "No"
            break

    print(ans)


if __name__ == "__main__":
    main()
