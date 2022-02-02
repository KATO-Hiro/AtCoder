# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    t = list(s)
    n = len(t)

    time = 500
    left_hand = [1, 2, 3, 4, 5]

    if int(s[0]) in left_hand:
        pre_hand = "left"
    else:
        pre_hand = "right"

    for i in range(1, n):
        cur_hand = ""

        if int(s[i]) in left_hand:
            cur_hand = "left"
        else:
            cur_hand = "right"

        if s[i] == s[i - 1]:
            time += 301
        elif cur_hand == pre_hand:
            time += 210
        else:
            time += 100
        
        pre_hand = cur_hand

    print(time)


if __name__ == "__main__":
    main()
