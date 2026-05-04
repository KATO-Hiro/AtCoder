# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    t = list(map(int, input().split()))
    s = [list(map(int, input().split())) for _ in range(n)]
    candidates = []

    for i, si in enumerate(s, 1):
        ok = True
        summed = 0

        for sij, ti in zip(si, t):
            if sij < ti:
                ok = False
                break

            summed += sij

        if not ok:
            continue

        candidates.append((summed, i))

    candidates.sort(reverse=True)
    size = len(candidates)
    inf = 10**18
    b = inf
    ans = []

    for i in range(min(size, k)):
        candidate, id = candidates[i]
        ans.append(id)
        b = min(b, candidate)

    if size >= k:
        for j in range(k, size):
            candidate, id = candidates[j]

            if candidate < b:
                break

            ans.append(id)

    ans.sort()

    for ans_i in ans:
        print(ans_i)


if __name__ == "__main__":
    main()
