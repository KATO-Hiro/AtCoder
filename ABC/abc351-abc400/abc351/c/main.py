# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = list()

    for ai in a:
        ans.append(ai)

        while len(ans) >= 2 and ans[-1] == ans[-2]:
            first = ans.pop()
            _ = ans.pop()
            ans.append(first + 1)

    print(len(ans))


if __name__ == "__main__":
    main()
