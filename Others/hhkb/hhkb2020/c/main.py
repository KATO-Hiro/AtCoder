# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    p = list(map(int, input().split()))

    is_used = [False for _ in range(2 * 10 ** 5 + 10)]
    index = 0

    for pi in p:
        is_used[pi] = True

        while is_used[index]:
            index += 1

        print(index)


if __name__ == "__main__":
    main()
