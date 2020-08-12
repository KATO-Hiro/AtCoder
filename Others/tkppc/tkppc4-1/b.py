# -*- coding: utf-8 -*-


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    index = -1
    candidate_a = 0

    for idx, ai in enumerate(a, 1):
        if candidate_a < ai < k:
            index = idx
            candidate_a = ai

    print(index)


if __name__ == '__main__':
    main()
