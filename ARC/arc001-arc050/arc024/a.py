# -*- coding: utf-8 -*-


def main():
    from collections import Counter

    left, right = map(int, input().split())
    left_shoes = Counter(list(map(int, input().split())))
    right_shoes = Counter(list(map(int, input().split())))
    pair_count = 0

    for left_size, left_shoe_count in left_shoes.items():
        if left_size in right_shoes.keys():
            pair_count += min(left_shoe_count, right_shoes[left_size])

    print(pair_count)


if __name__ == '__main__':
    main()
