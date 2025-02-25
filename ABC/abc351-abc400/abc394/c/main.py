# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    s = s[::-1]
    stack = list()

    for si in s:
        if si == "W":
            if len(stack) >= 1 and stack[-1] == "A":
                stack.pop()
                stack.append("C")
                stack.append("A")
            else:
                stack.append(si)
        else:
            stack.append(si)

    ans = stack[::-1]
    print("".join(ans))


if __name__ == "__main__":
    main()
