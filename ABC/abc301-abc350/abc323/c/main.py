# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [list(input().rstrip()) for _ in range(n)]
    total_scores = list()
    not_solved_all = list()

    for i, si in enumerate(s, 1):
        tmp = 0
        not_solved = list()

        for j, sij in enumerate(si):
            if sij == "o":
                tmp += a[j]
            else:
                not_solved.append(a[j])

        total_scores.append(tmp + i)
        not_solved_all.append(sorted(not_solved, reverse=True))

    max_score = max(total_scores)

    for i, total_score in enumerate(total_scores):
        count = 0
        tmp_score = total_score

        for not_solved_i in not_solved_all[i]:
            if tmp_score >= max_score:
                break

            tmp_score += not_solved_i
            count += 1

        print(count)


if __name__ == "__main__":
    main()
