# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    k = int(input())
    s = input().rstrip()[:-1]
    t = input().rstrip()[:-1]
    cs, ct = Counter(s), Counter(t)
    remain = [k] * 10
    remain[0] = 0

    for key, value in cs.items():
        remain[int(key)] -= value
    for key, value in ct.items():
        remain[int(key)] -= value

    count = 0

    def calc_score(u):
        score = 0

        for i in range(1, 10):
            score += int(i) * (10 ** u[str(i)])

        return score

    for i in range(1, 10):
        for j in range(1, 10):
            if i == j:
                if not (remain[i] >= 2):
                    continue

                cs[str(i)] += 1
                ct[str(j)] += 1

                score_t = calc_score(cs)
                score_a = calc_score(ct)

                if score_t > score_a:
                    count += remain[i] * (remain[i] - 1)

                cs[str(i)] -= 1
                ct[str(j)] -= 1
            else:
                if not (remain[i] >= 1 and remain[j] >= 1):
                    continue

                cs[str(i)] += 1
                ct[str(j)] += 1

                score_t = calc_score(cs)
                score_a = calc_score(ct)

                if score_t > score_a:
                    count += remain[i] * remain[j]

                cs[str(i)] -= 1
                ct[str(j)] -= 1

    total = (9 * k - 8) * (9 * k - 9)
    ans = count / total

    print(ans)


if __name__ == "__main__":
    main()
