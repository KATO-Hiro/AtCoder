# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    # 2進数
    # x, yの各bitを見たときに、両方とも1である集合Aと片方しかない集合Bを考える
    # 集合A、Bを使って、aとsを表す
    # Σ集合A = a、2 * Σ集合A + Σ集合B = s
    # Σ集合B = s - 2 * a

    # 条件
    # Σ集合B >= 0
    # 集合Aと集合Bの共通部分はない (= 共通部分は集合Aにしかないため)
    # a AND (s - 2 * a) = 0
    t = int(input())

    for _ in range(t):
        ai, si = map(int, input().split())

        diff = si - 2 * ai

        if diff >= 0 and ai & diff == 0:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
