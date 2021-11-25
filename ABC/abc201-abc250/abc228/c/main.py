# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    k -= 1
    scores = list()

    for i in range(n):
        pi = sum(list(map(int, input().split())))
        scores.append((pi, i))
    
    scores = sorted(scores, reverse=True)
    ans = list()

    for i, (score, index) in enumerate(scores):
        if i <= k:
            ans.append((index, "Yes"))
        else:
            if score + 300 >= scores[k][0]:
                ans.append((index, "Yes"))
            else:
                ans.append((index, "No"))

    for index, a in sorted(ans):
        print(a)


if __name__ == "__main__":
    main()
