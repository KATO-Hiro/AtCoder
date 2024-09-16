# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    sab, sac, sbc = input().rstrip().split()

    if sab == ">" and sac == ">" and sbc == ">":
        print("B")
    elif sab == "<" and sac == "<" and sbc == "<":
        print("B")
    elif sab == ">" and sac == ">" and sbc == "<":
        print("C")
    elif sab == "<" and sac == "<" and sbc == ">":
        print("C")
    elif sab == ">" and sac == "<" and sbc == "<":
        print("A")
    elif sab == "<" and sac == ">" and sbc == ">":
        print("A")


if __name__ == "__main__":
    main()
