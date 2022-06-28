# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, l = map(int, input().split())
    apples = list()

    for i in range(1, n + 1):
        taste = l + i - 1
        apples.append(taste)
    
    total = sum(apples)
    candidates = list()

    for i, apple in enumerate(apples):
        candidate = total - apple
        candidates.append((abs(total - candidate), candidate))
        
    print(sorted(candidates)[0][1])


if __name__ == "__main__":
    main()
