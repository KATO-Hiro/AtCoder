# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c, d = map(int, input().split())
    # 小数同士の比較による誤差を回避するため通分 + 分母BDが0以外のため、*BD
    left = a * b * (d**2)
    right = c * (b**2) * d

    if left < right:
        print("<")
    elif left > right:
        print(">")
    else:
        print("=")


if __name__ == "__main__":
    main()
