# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    q = int(input())
    cards = defaultdict(set)
    boxes = defaultdict(list)

    for _ in range(q):
        qi = list(map(int, input().split()))

        if qi[0] == 1:
            i, j = qi[1:]
            boxes[j].append(i)
            cards[i].add(j)
        elif qi[0] == 2:
            i = qi[1]
            print(*sorted(boxes[i]))
        else:
            i = qi[1]
            print(*sorted(cards[i]))


if __name__ == "__main__":
    main()
