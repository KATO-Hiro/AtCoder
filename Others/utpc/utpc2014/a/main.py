# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip().split(" ")
    # print(s)
    flag = False

    for i in range(len(s) - 1, -1, -1):
        if s[i] != "not":
            flag = True
        elif flag and s[i] == s[i + 1] == "not":
            s.pop(i)
            s.pop(i)

    print(*s)


if __name__ == "__main__":
    main()
