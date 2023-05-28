# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    t = input().rstrip()

    for (
        si,
        ti,
    ) in zip(s, t):
        if si == ti:
            pass
        elif (si == "1" and ti == "l") or (ti == "1" and si == "l"):
            pass
        elif (si == "0" and ti == "o") or (ti == "0" and si == "o"):
            pass
        else:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
