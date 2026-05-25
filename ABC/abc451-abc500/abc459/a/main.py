# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x = int(input())
    x -= 1
    s = "HelloWorld"
    n = len(s)
    ans = []

    for i in range(n):
        if i == x:
            continue

        ans.append(s[i])

    print("".join(ans))


if __name__ == "__main__":
    main()
