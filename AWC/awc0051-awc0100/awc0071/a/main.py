# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    count = 0
    candidates = [0]

    for si in s:
        if si == "(":
            count += 1
        else:
            count -= 1

        candidates.append(count)

    ans = max(candidates[:-1])
    print(ans)


if __name__ == "__main__":
    main()
