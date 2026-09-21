def main():
    import sys
    from itertools import pairwise, permutations

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print(0)
        sys.exit()

    score = 0

    for pattern in permutations(a):
        candidate = 0

        for first, second in pairwise(pattern):
            candidate += abs(first - second)

        score = max(score, candidate)

    print(score)


if __name__ == "__main__":
    main()
