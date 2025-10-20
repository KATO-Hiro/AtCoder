# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    q = int(input())
    stack = []
    summed = 0
    rev_count = 0

    for _ in range(q):
        query = input().rstrip().split()

        if query[0] == "1":
            c = query[1]

            stack.append(c)

            if c == "(":
                summed += 1
            else:
                summed -= 1

            if summed < 0 and c == ")":
                rev_count += 1
        else:
            prev = stack.pop()

            if prev == "(":
                summed -= 1
            else:
                summed += 1

            if summed <= 0 and prev == ")":
                rev_count -= 1

        if summed == 0 and rev_count == 0:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
