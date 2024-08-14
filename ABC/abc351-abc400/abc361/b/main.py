# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    # 1次元の区間の問題と言い換え、区間が重ならないと体積が正にならない
    # 各軸で条件を満たしているか判定
    x1, y1, z1, x2, y2, z2 = map(int, input().split())
    x3, y3, z3, x4, y4, z4 = map(int, input().split())

    def f(l1, r1, l2, r2):
        if r1 <= l2 or r2 <= l1:
            return False
        else:
            return True

    if f(x1, x2, x3, x4) and f(y1, y2, y3, y4) and f(z1, z2, z3, z4):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
