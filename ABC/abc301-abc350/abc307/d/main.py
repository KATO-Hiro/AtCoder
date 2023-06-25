# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    stack = deque()
    count = 0

    for si in s:
        stack.append(si)

        if si == "(":
            count += 1
        elif si == ")":
            while len(stack) > 0 and count > 0:
                sj = stack.pop()

                if sj == "(":
                    count -= 1
                    break

    print("".join(stack))


if __name__ == "__main__":
    main()
