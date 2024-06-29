# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    # 円環上の弦を数直線における区間の問題と言い換え
    # さらに、区間の問題を括弧列の対応関係に帰着
    # 括弧列が対応しているかどうかは、stackで判定できる
    n = int(input())
    p = [0] * 2 * n

    for i in range(n):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
        p[ai], p[bi] = i, i

    stack = list()

    for pi in p:
        if len(stack) >= 1 and pi == stack[-1]:
            stack.pop()
        else:
            stack.append(pi)

    if len(stack) >= 1:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
