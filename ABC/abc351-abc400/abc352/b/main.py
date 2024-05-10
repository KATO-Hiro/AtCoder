# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    t = input().rstrip()
    m = len(t)
    j = 0
    ans = list()

    for si in s:
        while j < m and t[j] != si:
            j += 1

        ans.append(j + 1)
        j += 1

    print(*ans)


if __name__ == "__main__":
    main()
