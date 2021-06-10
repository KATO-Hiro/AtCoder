# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    xy = list(map(int, input().split()))

    if len(set(xy)) == 1:
        print(xy[0])
    else:
        checked = [False for _ in range(3)]

        for hand in xy:
            checked[hand] = True

        for index, c in enumerate(checked):
            if not c:
                print(index)
                exit()


if __name__ == "__main__":
    main()
