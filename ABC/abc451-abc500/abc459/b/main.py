# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip().split()
    ans = []

    for si in s:
        if si[0] in ["a", "b", "c"]:
            ans += "2"
        elif si[0] in ["d", "e", "f"]:
            ans += "3"
        elif si[0] in ["g", "h", "i"]:
            ans += "4"
        elif si[0] in ["j", "k", "l"]:
            ans += "5"
        elif si[0] in ["m", "n", "o"]:
            ans += "6"
        elif si[0] in ["p", "q", "r", "s"]:
            ans += "7"
        elif si[0] in ["t", "u", "v"]:
            ans += "8"
        else:
            ans += "9"

    print("".join(ans))


if __name__ == "__main__":
    main()
