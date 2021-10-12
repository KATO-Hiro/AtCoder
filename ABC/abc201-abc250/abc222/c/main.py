# -*- coding: utf-8 -*-


def judge(first_hand, second_hand):
    # -1: draw
    # 0: first_hand win
    # 1: second_hand win

    if first_hand == second_hand:
        return -1
    elif first_hand == 'G' and second_hand == 'C':
        return 0
    elif first_hand == 'C' and second_hand == 'P':
        return 0
    elif first_hand == 'P' and second_hand == 'G':
        return 0
    
    return 1


def main():
    n, m = map(int, input().split())
    a = [list(input()) for _ in range(2 * n)]
    win_count = [0] * (2 * n)

    for j in range(m):
        order = [(count, index) for index, count in enumerate(win_count)]
        sorted_order = sorted(order, key=lambda x: (x[0], -x[1]) ,reverse=True)

        for i in range(n):
            first_id = sorted_order[2 * i][1]
            first_hand = a[first_id][j]

            second_id = sorted_order[2 * i + 1][1]
            second_hand = a[second_id][j]

            result = judge(first_hand, second_hand)

            if result == 0:
                win_count[first_id] += 1
            elif result == 1:
                win_count[second_id] += 1
    
    order = [(count, index) for index, count in enumerate(win_count)]
    sorted_order = sorted(order, key=lambda x: (x[0], -x[1]) ,reverse=True)

    for _, index in sorted_order:
        print(index + 1)


if __name__ == "__main__":
    main()
