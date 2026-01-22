# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    stack = []

    for ai in a:
        if len(stack) >= 3 and ai == stack[-3] == stack[-2] == stack[-1]:
            for _ in range(3):
                stack.pop()
        else:
            stack.append(ai)

    print(len(stack))


if __name__ == "__main__":
    main()
