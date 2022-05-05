# -*- coding: utf-8 -*-


def calc(c):
    # See:
    # https://www.youtube.com/watch?v=igfVeTsGeYw
    # 0 ^ 1、2 ^ 3、...が1になることを活用
    count_one = (c + 1) // 2 # 1の個数を数える
    ans = count_one % 2  # xorを取ったときに、偶数なら0、奇数なら1を返す

    # 偶数のときは、はみ出た部分を考慮
    if c % 2 == 0:
        ans ^= c
    
    return ans


def main():
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())

    # [a, b] = [0, b] ^ [a, 0]と言い換えることができる
    ans = calc(b) ^ calc(a - 1)
    print(ans)


if __name__ == "__main__":
    main()
