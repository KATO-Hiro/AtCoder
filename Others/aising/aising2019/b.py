# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a, b = map(int, input().split())
    p = list(map(int, input().split()))
    group_1 = list()
    group_2 = list()
    group_3 = list()

    for pi in p:
        if pi <= a:
            group_1.append(pi)
        elif pi > b:
            group_3.append(pi)
        else:
            group_2.append(pi)

    print(min(len(group_1), len(group_2), len(group_3)))


if __name__ == '__main__':
    main()
