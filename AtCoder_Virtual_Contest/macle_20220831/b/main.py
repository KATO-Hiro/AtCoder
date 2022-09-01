# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    colors = [0] * 9  # 灰、茶、緑、水、青、黄、橙、赤、自由

    for ai in a:
        if ai >= 3200:
            colors[8] += 1
        elif 2800 <= ai < 3200:
            colors[7] += 1
        elif 2400 <= ai < 2800:
            colors[6] += 1
        elif 2000 <= ai < 2400:
            colors[5] += 1
        elif 1600 <= ai < 2000:
            colors[4] += 1
        elif 1200 <= ai < 1600:
            colors[3] += 1
        elif 800 <= ai < 1200:
            colors[2] += 1
        elif 400 <= ai < 800:
            colors[1] += 1
        else:
            colors[0] += 1
    
    ans_min, ans_max = 0, 0

    for i in range(9):
        if i == 8:
            if ans_min == 0:
                ans_min += 1

            ans_max += colors[8]
        else:
            if colors[i] >= 1:
                ans_min += 1
                ans_max += 1
    
    print(ans_min, ans_max)


if __name__ == "__main__":
    main()
