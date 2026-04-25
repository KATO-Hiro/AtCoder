# -*- coding: utf-8 -*-

import sys

input = sys.stdin.readline


def f(s):
    stack = []

    for si in s:
        stack.append(si)

        if len(stack) <= 3:
            continue
        if (
            stack[-4] == "("
            and stack[-3] == "x"
            and stack[-2] == "x"
            and stack[-1] == ")"
        ):
            for _ in range(4):
                stack.pop()

            stack.append("x")
            stack.append("x")

    return "".join(stack)


def solve():
    a = input().rstrip()
    b = input().rstrip()

    if f(a) == f(b):
        print("Yes")
    else:
        print("No")


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
