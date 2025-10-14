# -*- coding: utf-8 -*-


def digit_sum(number: int) -> int:
    return sum(map(int, list(str(number))))


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = [1]

    for i in range(n - 1):
        prev = ans[-1]

        candidate = prev + digit_sum(prev)
        ans.append(candidate)

    print(ans[-1])


if __name__ == "__main__":
    main()
