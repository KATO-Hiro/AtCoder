# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    left_count = 0
    right_count = 0
    ans = ''

    for si in s:
        if si == "(":
            left_count += 1
            ans += si
        else:
            right_count += 1
            ans += si

            if right_count > left_count:
                ans = '(' + ans
                left_count += 1

    while left_count > right_count:
        ans += ')'
        right_count += 1

    print(ans)


if __name__ == "__main__":
    main()
