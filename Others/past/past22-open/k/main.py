# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    inf = 10**9
    stack = [(inf, -1)]
    ans = []

    for i, ai in enumerate(a, 1):
        while stack and ai > stack[-1][0]:
            stack.pop()

        ans.append(stack[-1][1])
        stack.append((ai, i))

    print(*ans)


if __name__ == "__main__":
    main()
