# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    ans = list()
    prev = "0"
    remain = n

    for si in reversed(list(s)):
        if si != prev:
            if si == "0":
                ans.append("B" * remain)
            else:
                ans.append("A" * remain)

        prev = si
        remain -= 1

    ans = "".join(ans)
    print(len(ans))
    print(ans)


if __name__ == "__main__":
    main()
