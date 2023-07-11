# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    stack = deque()
    ans = deque()

    # for si in s:
    #     if si == "(":
    #         stack.append("(")
    #     else:
    #         if len(stack) > 0:
    #             ans.append(stack.pop())
    #         else:
    #             ans.appendleft("(")

    #         ans.append(")")

    # if len(stack) > 0:
    #     count = 0

    #     while stack:
    #         ans.append(stack.pop())
    #         count += 1

    #     for _ in range(count):
    #         ans.append(")")

    # print("".join(map(str, ans)))


if __name__ == "__main__":
    main()
