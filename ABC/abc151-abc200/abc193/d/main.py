# -*- coding: utf-8 -*-


def main():
    k = int(input())
    s = input()
    t = input()
    numbers = [k for _ in range(10)]
    t_numbers = [0 for _ in range(10)]
    a_numbers = [0 for _ in range(10)]

    for si, ti in zip(s[:-1], t[:-1]):
        numbers[int(si)] -= 1
        numbers[int(ti)] -= 1

        t_numbers[int(si)] += 1
        a_numbers[int(ti)] += 1

    count = 0

    for i in range(1, 10):
        for j in range(1, 10):
            if numbers[i] == 0:
                continue

            if numbers[i] == 1 and i == j:
                continue

            t_score = 0
            a_score = 0

            for num in range(1, 10):
                if num == i:
                    t_score += num * (10 ** (t_numbers[num] + 1))
                else:
                    t_score += num * (10 ** t_numbers[num])

                if num == j:
                    a_score += num * (10 ** (a_numbers[num] + 1))
                else:
                    a_score += num * (10 ** a_numbers[num])

            if t_score > a_score:
                if i != j:
                    count += numbers[i] * numbers[j]
                else:
                    count += numbers[i] * (numbers[j] - 1)

    c = k * 9 - 8
    total_pattern = c * (c - 1)
    print(count / total_pattern)


if __name__ == "__main__":
    main()
