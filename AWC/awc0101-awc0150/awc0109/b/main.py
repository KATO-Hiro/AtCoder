# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    stack = []

    for si in s:
        if len(stack) == 0:
            stack.append(si)
            continue

        if si == stack[-1]:
            stack.pop()
        else:
            stack.append(si)

    print(len(stack))


if __name__ == "__main__":
    main()
