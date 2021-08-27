# -*- coding: utf-8 -*-


def digit_sum(n):
    summed = 0

    while n > 0:
        summed += n % 10
        n //= 10

    return summed


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    mod = 10 ** 5

    next_pos = [0] * mod

    # 前計算: 値xのときに、次の値がいくつになるか?
    for x in range(mod):
        y = digit_sum(x)
        z = (x + y) % mod
        next_pos[x] = z
    
    histories = [-1] * mod
    cur_pos, count = n, 0

    # 2周目となる最初の値を検出
    while histories[cur_pos] == -1:
        histories[cur_pos] = count
        cur_pos = next_pos[cur_pos]
        count += 1
    
    # 周期を求める
    cycle = count - histories[cur_pos]

    # 周期+αのαを求める
    if k >= histories[cur_pos]:
        k = (k - histories[cur_pos]) % cycle + histories[cur_pos]

    # α回押したときの整数を求める
    for i in range(mod):
        if histories[i] == k:
            print(i)
            exit()


if __name__ == "__main__":
    main()
