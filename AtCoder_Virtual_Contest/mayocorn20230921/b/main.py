# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = [list(input().rstrip()) for _ in range(2 * n)]
    scores = [(0, i) for i in range(2 * n)]
    # print(a)
    # print(scores)

    for j in range(m):
        scores = sorted(scores, key=lambda x: (x[0], -x[1]), reverse=True)
        new_scores = list()

        for i in range(n):
            first_score, first_id = scores[2 * i]
            second_score, second_id = scores[2 * i + 1]

            first_hand, second_hand = a[first_id][j], a[second_id][j]

            if first_hand == "G" and second_hand == "C":
                first_score += 1
            elif first_hand == "C" and second_hand == "G":
                second_score += 1
            elif first_hand == "C" and second_hand == "P":
                first_score += 1
            elif first_hand == "P" and second_hand == "C":
                second_score += 1
            elif first_hand == "P" and second_hand == "G":
                first_score += 1
            elif first_hand == "G" and second_hand == "P":
                second_score += 1

            new_scores.append((first_score, first_id))
            new_scores.append((second_score, second_id))

        scores = new_scores

    final_scores = sorted(scores, key=lambda x: (x[0], -x[1]), reverse=True)

    # print(final_scores)

    for score, id in final_scores:
        print(id + 1)


if __name__ == "__main__":
    main()
