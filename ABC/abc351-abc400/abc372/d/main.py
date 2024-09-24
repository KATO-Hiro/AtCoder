# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    h = list(map(int, input().split()))
    stack = []
    ans = []

    for hi in h[::-1]:
        ans.append(len(stack))

        while stack and stack[-1] < hi:
            stack.pop()

        stack.append(hi)

    print(*ans[::-1])


if __name__ == "__main__":
    main()
