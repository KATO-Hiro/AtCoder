# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    k = int(input())

    # kの倍数をmod k = 0と言い換え
    # 漸化式を立てる
    a = [7 % k]

    for i in range(2, k + 1):
        a.append((a[-1] * 10 + 7) % k)
    
    for i, ai in enumerate(a, 1):
        if ai == 0:
            print(i)
            exit()

    print(-1)


if __name__ == "__main__":
    main()
