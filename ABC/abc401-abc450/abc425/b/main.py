# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import permutations

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))

    for pattern in permutations(range(1, n + 1)):
        ok = True

        for ai, pi in zip(a, pattern):
            if ai != -1 and pi != ai:
                ok = False
                break

        if ok:
            print("Yes")
            print(*pattern)
            exit()

    print("No")


if __name__ == "__main__":
    main()
