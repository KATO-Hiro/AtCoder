# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    t = ["ACE", "BDF", "CEG", "DFA", "EGB", "FAC", "GBD"]

    s = input().rstrip()

    if s in t:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
