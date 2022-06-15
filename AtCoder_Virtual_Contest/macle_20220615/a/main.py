# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x = map(int, input().split())
    s = input().rstrip()
    score = x

    for si in s:
        if si == "o":
            score += 1
        elif si == "x" and score > 0:
            score -= 1
    
    print(score)


if __name__ == "__main__":
    main()
