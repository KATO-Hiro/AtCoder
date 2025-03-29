# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    pos = 0
    ans = list()
    PENDING = -1

    def find(cur_pos, comment):
        for i in range(cur_pos, n):
            if i + 1 < n and s[i : i + 2] == comment:
                return i

        return PENDING

    while True:
        i = find(pos, "/*")

        if i == PENDING:
            break

        j = find(i + 2, "*/")

        if j == PENDING:
            break

        ans += s[pos:i]
        pos = j + 2

    ans += s[pos:]

    print(*ans, sep="")


if __name__ == "__main__":
    main()
