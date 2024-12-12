# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict, deque

    input = sys.stdin.readline

    n = int(input())
    x, y = input().rstrip().split()
    d = defaultdict(list)
    q = deque([x])

    for _ in range(n):
        si, ti = input().rstrip().split()

        if d[si]:
            d[si].append(ti)
        else:
            d[si] = [ti]

    used = set()

    while q:
        qi = q.popleft()

        if qi == y:
            print("Yes")
            exit()

        if qi in used:
            continue

        used.add(qi)

        for to in d[qi]:
            if to == qi:
                continue
            if to in used:
                continue

            q.append(to)

    print("No")


if __name__ == "__main__":
    main()
