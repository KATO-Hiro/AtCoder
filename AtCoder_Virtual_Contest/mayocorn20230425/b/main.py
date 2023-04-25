# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()

    if s[0] == "A" and s[2:-1].count("C") == 1:
        t = s.replace("A", "").replace("C", "")

        for ti in t:
            if not ti.islower():
                print("WA")
                exit()

        print("AC")
    else:
        print("WA")


if __name__ == "__main__":
    main()
