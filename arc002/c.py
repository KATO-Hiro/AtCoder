# -*- coding: utf-8 -*-


def main():
    from itertools import combinations

    n = int(input())
    c = input()
    commands = ['A', 'B', 'X', 'Y']
    shortcuts = list()
    ans = float('inf')

    for c1 in commands:
        for c2 in commands:
            shortcuts.append(c1 + c2)

    # L, Rに割り当てる組み合わせをすべて試す
    for left, right in list(combinations(shortcuts, 2)):
        dummy = c
        dummy = dummy.replace(left, 'L')
        dummy = dummy.replace(right, 'R')
        ans = min(ans, len(dummy))

    print(ans)


if __name__ == '__main__':
    main()
