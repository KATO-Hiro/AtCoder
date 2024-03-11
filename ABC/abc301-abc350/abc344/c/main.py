# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    l = int(input())
    c = list(map(int, input().split()))
    q = int(input())
    x = list(map(int, input().split()))
    numbers = set()

    for ai in a:
        for bj in b:
            for ck in c:
                numbers.add(ai + bj + ck)

    # print(numbers)

    for xi in x:
        if xi in numbers:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
