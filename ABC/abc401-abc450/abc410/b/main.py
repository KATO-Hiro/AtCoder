# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    x = list(map(int, input().split()))
    size_max = 110
    boxes = [[] for _ in range(size_max)]

    for i, xi in enumerate(x):
        if xi >= 1:
            boxes[xi - 1].append(i)
        else:
            size, id = 10**9, -1

            for j in range(n):
                now = len(boxes[j])

                if now < size:
                    size = now
                    id = j

            boxes[id].append(i)

    ans = [0] * q

    for i, box in enumerate(boxes, 1):
        for b in box:
            ans[b] = i

    print(*ans)


if __name__ == "__main__":
    main()
