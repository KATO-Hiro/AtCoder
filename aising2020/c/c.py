# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    ans = [0 for _ in range(10 ** 6 + 2000)]
    candidate = 110

    # KeyInsight:
    # ◯: 範囲を限定して全探索
    # ×: 最大ケースに、それ未満のケースが含まれる場合は、最大ケースだけ考える
    for x in range(1, candidate + 1):
        for y in range(1, candidate + 1):
            for z in range(1, candidate + 1):
                total = 0
                total += (x ** 2) + (y ** 2) + (z ** 2)
                total += (x * y) + (y * z) + (z * x)

                if total < (10 ** 6 + 2000):
                    ans[total] += 1

    for i in range(1, n + 1):
        print(ans[i])


if __name__ == '__main__':
    main()
