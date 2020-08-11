# -*- coding: utf-8 -*-


def main():
    n, m = map(int, input().split())
    num = [1 for _ in range(n)]
    red = [False for _ in range(n)]
    red[0] = True

    # Key Insight
    # 問題を言い換える
    # num[i] := i番目のコップに入っている水の量
    # red[i] := i番目のコップに赤い水が入っているか
    for i in range(m):
        xi, yi = map(int, input().split())
        xi -= 1
        yi -= 1

        if red[xi]:
            red[yi] = True

        num[xi] -= 1
        num[yi] += 1

        # 移動前のコップに入っていたのが赤い水だけだったとき
        if num[xi] == 0:
            red[xi] = False

    print(sum(red))


if __name__ == '__main__':
    main()
