# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    w, b = map(int, input().split())
    s = "wbwbwwbwbwbw" * 25
    m = len(s)

    for i in range(m):
        for j in range(i + 1, m + 1):
            t = s[i:j]

            if t.count("w") == w and t.count("b") == b:
                print("Yes")
                exit()

    print("No")


if __name__ == "__main__":
    main()
