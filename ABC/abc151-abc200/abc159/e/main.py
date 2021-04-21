# -*- coding: utf-8 -*-


def can_add(j, k, t, group, group_id):
    for index in range(group_id):
        group[index] += t[index][j]

        if group[index] > k:
            return False, group

    return True, group


def main():
    import sys

    input = sys.stdin.readline

    h, w, k = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(h)]
    t = [[0 for __ in range(w)] for _ in range(h)]
    ans = float("inf")

    for bit in range(1 << (h - 1)):
        id = [0 for _ in range(h)]
        current_id = 0

        for j in range(h):
            id[j] = current_id

            if bit & (1 << j):
                current_id += 1

        current_id += 1

        # Initialize
        for wi in range(w):
            for hi in range(h):
                t[hi][wi] = 0

        # Count white choco in each group.
        for wi in range(w):
            for hi in range(h):
                t[id[hi]][wi] += int(s[hi][wi])

        ok = True

        for wi in range(w):
            for hi in range(h):
                if t[id[hi]][wi] > k:
                    ok = False

        if not ok:
            continue

        candidate = current_id - 1
        group = [0 for _ in range(current_id)]

        for wj in range(w):
            flag, group = can_add(wj, k, t, group, current_id)

            if not flag:
                candidate += 1
                group = [t[i][wj] for i in range(current_id)]

        ans = min(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()
