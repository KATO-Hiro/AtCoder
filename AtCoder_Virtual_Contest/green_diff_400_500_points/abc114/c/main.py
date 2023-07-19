# -*- coding: utf-8 -*-


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    s = input().rstrip()
    d = len(s)
    n = int(s)
    numbers = list()

    def dfs(i, upper_digit):
        if i == upper_digit:
            digit_count = len(set(numbers))
            number = int("".join(numbers))

            if digit_count == 3 and number <= n:
                return 1
            else:
                return 0

        ans = 0

        for number in ["3", "5", "7"]:
            numbers.append(number)
            ans += dfs(i + 1, upper_digit)
            numbers.pop()

        return ans

    ans = 0

    for i in range(3, d + 1):
        ans += dfs(0, i)

    print(ans)


if __name__ == "__main__":
    main()
