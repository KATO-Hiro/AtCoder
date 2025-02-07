# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    stack = list()

    for si in s:
        if si != ")":
            stack.append(si)
        else:
            t = list()

            while stack:
                if stack[-1] == "(":
                    stack.pop()
                    break

                t.append(stack.pop())

            u = t[::-1] + t

            for ui in u:
                stack.append(ui)

    print("".join(stack))


if __name__ == "__main__":
    main()
