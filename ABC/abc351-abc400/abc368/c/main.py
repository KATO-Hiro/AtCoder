# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    h = list(map(int, input().split()))
    t = 0

    # 周期性を活用して、ちょうどp周 + 端数qに分解
    # 1周で体力を5削れる + 残りは愚直にシミュレーション
    for hi in h:
        pi, qi = divmod(hi, 5)
        t += 3 * pi

        while qi > 0:
            # 先にインクリメントしておくのがポイント
            t += 1

            if t % 3 == 0:
                qi -= 3
            else:
                qi -= 1

    print(t)


if __name__ == "__main__":
    main()
