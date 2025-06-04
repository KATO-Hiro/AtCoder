# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    stack = []

    for si in s:
        if si == "x" and len(stack) >= 2 and stack[-2] == "f" and stack[-1] == "o":
            stack.pop()
            stack.pop()
        else:
            stack.append(si)

    print(len(stack))


if __name__ == "__main__":
    main()
