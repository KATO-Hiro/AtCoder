# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    k = int(input())
    x = 7 % k  # k == 7の場合への対処

    # KeyInsight:
    # ◯: Mod kを取る
    # ◯: 値が(x * 10 + 7)ずつ増えていく
    # △: Modを取った後の演算について理解が浅かった
    for i in range(1, k + 1):
        if x == 0:
            print(i)
            exit()

        x = (x * 10 + 7) % k

    print(-1)


if __name__ == '__main__':
    main()
