# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    k -= 1
    scores = list()

    for i in range(n):
        pi = sum(list(map(int, input().split())))
        scores.append(pi)
    
    border = sorted(scores, reverse=True)[k]

    for score in scores:
        if score + 300 >= border:
            print('Yes')
        else:
            print('No')


if __name__ == "__main__":
    main()
