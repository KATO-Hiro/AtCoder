# -*- coding: utf-8 -*-


def main():
    s = input()
    l, r = map(int, input().split())

    n = int(s)

    if s[0] == "0" and len(s) != 1:
        print("No")
        exit()

    if l <= n <= r:
        print('Yes')
    else:
        print("No")


if __name__ == "__main__":
    main()
