# -*- coding: utf-8 -*-


def main():
    from collections import Counter

    n, k = map(int, input().split())
    s = Counter([input() for _ in range(n)])

    word_count = sorted(list(s.values()), reverse=True)
    count = word_count[k - 1]

    if word_count.count(count) == 1:
        print(s.most_common()[k - 1][0])
    else:
        print("AMBIGUOUS")


if __name__ == "__main__":
    main()
