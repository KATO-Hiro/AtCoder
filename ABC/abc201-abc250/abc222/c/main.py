# -*- coding: utf-8 -*-


def main():
    n, m = map(int, input().split())
    a = [list(input()) for _ in range(2 * n)]
    win_count = [0] * (2 * n)

    for j in range(m):
        order = [(count, index) for index, count in enumerate(win_count)]
        sorted_order = sorted(order, key=lambda x: (x[0], -x[1]) ,reverse=True)
        aj = [a[i][j] for i in range(2 * n)]

        for i in range(n):
            first_id = sorted_order[2 * i][1]
            second_id = sorted_order[2 * i + 1][1]

            first_hand = aj[first_id]
            second_hand = aj[second_id]

            if first_hand == 'G' and second_hand == 'C':
                win_count[first_id] += 1
            elif first_hand == 'C' and second_hand == 'G':
                win_count[second_id] += 1
            elif first_hand == 'C' and second_hand == 'P':
                win_count[first_id] += 1
            elif first_hand == 'P' and second_hand == 'C':
                win_count[second_id] += 1
            elif first_hand == 'P' and second_hand == 'G':
                win_count[first_id] += 1
            elif first_hand == 'G' and second_hand == 'P':
                win_count[second_id] += 1
    
    order = [(count, index) for index, count in enumerate(win_count)]
    sorted_order = sorted(order, key=lambda x: (x[0], -x[1]) ,reverse=True)

    for _, index in sorted_order:
        print(index + 1)


if __name__ == "__main__":
    main()
