# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip().split()
    k = int(input())

    def div(a, b):
        if (a < 0) ^ (b < 0):
            return -((-a) // b)

        return a // b

    def f(u):
        stack = []

        for ui in u:
            stack.append(ui)

            while (
                len(stack) >= 3
                and stack[-3] in "+-*/"
                and stack[-2] not in "+-*/"
                and stack[-1] not in "+-*/"
            ):
                b = stack.pop()
                a = stack.pop()
                op = stack.pop()
                a, b = int(a), int(b)

                if op == "+":
                    tmp = a + b
                elif op == "-":
                    tmp = a - b
                elif op == "*":
                    tmp = a * b
                else:
                    tmp = div(a, b)

                stack.append(str(tmp))

        return stack[-1]

    before = f(s)

    if k > 0:
        t = list(s[:])
        p = list(map(int, input().split()))

        for pi in p:
            pi -= 1
            op = s[pi]

            if op == "+":
                t[pi] = "-"
            elif op == "-":
                t[pi] = "+"
            elif op == "*":
                t[pi] = "/"
            else:
                t[pi] = "*"

        after = f(t)
    else:
        after = before

    print(before)
    print(after)


if __name__ == "__main__":
    main()
