# -*- coding: utf-8 -*-


def count_squares(d, k):
    ans = 0

    # サンプルの図で，左下を原点とみなす
    for i in range(d // k + 1):
        for j in range(d // k + 1):
            count = 0

            # 正方形の4点が円の内側にあるかどうかを判定
            for m in [0, 1]:
                for n in [0, 1]:
                    # 正方形の位置と円の中心位置との差分を取る
                    dist = (d // 2 - (i + m) * k) ** 2 + (d // 2 - (j + n) * k) ** 2

                    if dist <= (d // 2) ** 2:
                        count += 1

            if count == 4:
                ans += 1

    return ans


def main():
    k = int(input())
    print(count_squares(200, k), count_squares(300, k))


if __name__ == '__main__':
    main()
