# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    numbers = list()
    i = 1

    while i**2 <= n:
        numbers.append(i**2)
        i += 1

    m = len(numbers)
    candidates = [0] * (n + 1)

    for i in range(m):
        for j in range(i + 1, m):
            summed = numbers[i] + numbers[j]

            if summed > n:
                break

            candidates[summed] += 1

    count = 0
    ans = list()

    for i, candidate in enumerate(candidates):
        if candidate != 1:
            continue

        count += 1
        ans.append(i)

    print(count)
    print(*ans)


if __name__ == "__main__":
    main()
