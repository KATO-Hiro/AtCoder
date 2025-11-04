# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    pos = list()

    for i, si in enumerate(s):
        if si != "X":
            continue

        pos.append(i)

    front, back = pos
    ans = s[:front] + s[front + 1 : back][::-1] + s[back + 1 :]
    print(ans)


if __name__ == "__main__":
    main()
