# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    lowers, uppers = [], []

    for si in s:
        if si.islower():
            lowers.append(si)
        else:
            uppers.append(si)

    print("".join(uppers))
    print("".join(lowers))


if __name__ == "__main__":
    main()
