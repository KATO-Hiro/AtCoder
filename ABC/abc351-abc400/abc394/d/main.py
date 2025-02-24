# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    stack = list()

    for si in s:
        if si == "(" or si == "[" or si == "<":
            stack.append(si)
        else:
            if len(stack) == 0:
                stack.append(si)
            else:
                prev = stack[-1]

                if si == ")" and prev == "(":
                    stack.pop()
                elif si == "]" and prev == "[":
                    stack.pop()
                elif si == ">" and prev == "<":
                    stack.pop()
                else:
                    stack.append(si)

    if len(stack) == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
