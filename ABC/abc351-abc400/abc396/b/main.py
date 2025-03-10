# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    q = int(input())
    stack = [0] * 100

    for _ in range(q):
        qi = list(map(int, input().split()))

        if qi[0] == 1:
            xi = qi[1]
            stack.append(xi)
        else:
            result = stack.pop()
            print(result)


if __name__ == "__main__":
    main()
