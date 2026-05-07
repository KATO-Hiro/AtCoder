# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    count = 0

    for ai in a:
        for bj in b:
            for ck in c:
                if sorted([ai, bj, ck]) == [4, 5, 6]:
                    count += 1

    ans = count / (6**3)
    print(ans)


if __name__ == "__main__":
    main()
