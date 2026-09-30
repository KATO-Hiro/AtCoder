# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    right = 1
    ans = 0

    for left in range(1, n):
        while right < n:
            if right + 1 == left:
                right += 1

            print("?", left, right + 1, flush=True)
            response = input().rstrip()

            if response == "Yes":
                right += 1
            else:
                break

        ans += right - left

    print("!", ans, flush=True)


if __name__ == "__main__":
    main()
