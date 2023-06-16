# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()

    # 最終的な状態から考える
    # 連続した3つのタイルが同じ色で塗られている = Yes
    for i in range(n):
        if i + 2 >= n:
            continue

        if s[i] == s[i + 1] == s[i + 2]:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
