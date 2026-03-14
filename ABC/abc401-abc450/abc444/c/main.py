# -*- coding: utf-8 -*-


def judge(array, candidate):
    while array and array[-1] == candidate:
        array.pop()

    size = len(array)

    if size % 2 == 1:
        return

    for i in range(size // 2):
        if array[i] + array[size - 1 - i] != candidate:
            return

    print(candidate)


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = sorted(list(map(int, input().split())))

    judge(a[:], a[-1])
    judge(a[:], a[0] + a[-1])


if __name__ == "__main__":
    main()
