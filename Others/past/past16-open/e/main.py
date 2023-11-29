# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()

    if s[0] == "1":
        if len(s) == 1:
            print(0)
        else:
            t = s[1:]

            if len(set(t)) == 1 and "0" in t:
                print(len(t))
            else:
                print(len(s))
    else:
        print(len(s))


if __name__ == "__main__":
    main()
