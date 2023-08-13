# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list()

    for i in range(1, n + 1):
        _ = int(input())
        ai = list(map(int, input().split()))
        a.append(ai)

    x = int(input())
    people = list()
    c_min = 100

    for i, ai in enumerate(a, 1):
        if x not in ai:
            continue

        c = len(ai)

        if c < c_min:
            c_min = c
            people = list()
            people.append(i)
        elif c == c_min:
            people.append(i)

        # print(i, c, people)

    size = len(people)
    print(size)

    if size > 0:
        print(*people)


if __name__ == "__main__":
    main()
