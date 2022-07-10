# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    t, n = map(int, input().split())
    score = [0] * n
    
    for i in range(t):
        p = list(map(int, input().split()))

        for j, pi in enumerate(p):
            score[j] = max(score[j], pi)
        
        print(sum(score))


if __name__ == "__main__":
    main()
