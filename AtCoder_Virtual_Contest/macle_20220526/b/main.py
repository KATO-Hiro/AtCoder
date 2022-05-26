# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    from collections import deque
    import sys

    input = sys.stdin.readline

    n = int(input())
    costs = [0] * n
    skills = defaultdict(list)

    for i in range(n):
        tka = list(map(int, input().split()))
        ti, ki = tka[0], tka[1]
        costs[i] = ti

        if ki > 0:
            ai = tka[2:]
            skills[i] = ai

    q = deque()
    q.append(n - 1)
    used = [False] * n
    ans = 0

    while q:
        qi = q.popleft()

        if used[qi]:
            continue

        used[qi] = True
        ans += costs[qi]

        for skill in skills[qi]:
            if not used[skill - 1]:
                q.append(skill - 1)

    print(ans)


if __name__ == "__main__":
    main()
