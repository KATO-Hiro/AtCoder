# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    # ゲーム: 後ろから見る
    # 直前のターンの期待値が、現在の出目より大きいときだけゲームを続行
    ans = 0.0

    for i in range(n):
        now = 0.0

        for die in range(1, 6 + 1):
            now += max(ans, die)
        
        now /= 6
        ans = now

    print(ans)


if __name__ == "__main__":
    main()
