# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x = int(input())

    # 等差数を満たす条件を列挙(基本は等差数列 + 問題特有の要素)
    # 初項a: [1, 9]
    # 公差d: [-9, 8]、各桁の数が[0, 9]であるため
    # 桁数n: [1, 18]、最大ケースである10 ** 17の場合、1が18個並んだ数であるため
    # 各桁の数: [0, 9]

    # 大雑把な計算量 < 10 * 20 * 20 = 4 * 10 ** 3なので、全探索できる
    # 条件を満たす数のうち、x以上で最小値が答え
    candidates = list()

    for a in range(1, 9 + 1):
        for d in range(-9, 8 + 1):
            number = ""

            for n in range(1, 18 + 1):
                value = a + d * (n - 1)

                if not (0 <= value <= 9):
                    break

                number += str(value)
                candidate = int(number)

                if candidate >= x:
                    candidates.append(candidate)

    print(min(candidates))


if __name__ == "__main__":
    main()
