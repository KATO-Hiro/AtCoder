# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    t = ""

    for si in s:
        if si == "6":
            t += "9"
        elif si == "9":
            t += "6"
        else:
            t += si
    
    print(''.join(reversed(t)))


if __name__ == "__main__":
    main()
