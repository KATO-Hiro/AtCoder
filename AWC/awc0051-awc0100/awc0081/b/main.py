# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    stack = []
    h = 0
    ans = 0

    for _ in range(n):
        di, vi = map(int, input().split())

        if di > h:
            stack.append((di, vi))
        else:
            ans += vi
            h += di

            while stack:
                if stack[-1][0] > h:
                    break
                else:
                    stack.pop()
                    ans += vi
                    h += di

    while stack:
        if stack[-1][0] > h:
            break
        else:
            stack.pop()
            ans += vi
            h += di

    print(ans)


if __name__ == "__main__":
    main()
