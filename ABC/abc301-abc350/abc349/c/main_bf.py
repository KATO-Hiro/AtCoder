# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    t = input().rstrip().lower()
    n = len(s)

    for i in range(n):
        for j in range(i + 1, n):
            tmp = s[i] + s[j]

            if tmp + "x" in t:
                print("Yes")
                exit()

            for k in range(j + 1, n):
                if tmp + s[k] in t:
                    print("Yes")
                    exit()

    print("No")


if __name__ == "__main__":
    main()
