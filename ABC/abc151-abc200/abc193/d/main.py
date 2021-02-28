# -*- coding: utf-8 -*-


def calc_score(s):
    count = [0 for _ in range(10)]
    score = 0

    for si in s:
        count[int(si)] += 1

    for num, c in enumerate(count):
        score += num * (10 ** c)

    return score


def main():
    k = int(input())
    s = input()
    t = input()
    numbers = [k for _ in range(10)]

    for si, ti in zip(s[:-1], t[:-1]):
        numbers[int(si)] -= 1
        numbers[int(ti)] -= 1

    count = 0

    for i in range(1, 10):
        for j in range(1, 10):
            t_score = calc_score(s[:-1] + str(i))
            a_score = calc_score(t[:-1] + str(j))

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
