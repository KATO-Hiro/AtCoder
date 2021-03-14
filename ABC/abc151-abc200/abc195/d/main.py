# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, q = map(int, input().split())
    wv = sorted([tuple(map(int, input().split())) for _ in range(n)])
    x = list(map(int, input().split()))

    for qi in range(q):
        li, ri = map(int, input().split())
        li -= 1
        ri -= 1

        boxes = list()

        for i in range(m):
            if li <= i <= ri:
                continue

            boxes.append(x[i])

        boxes = sorted(boxes)
        is_used = [False for _ in range(n)]
        ans = 0

        for box in boxes:
            best_value, index = -1, -1

            for i in range(n):
                if is_used[i]:
                    continue

                if wv[i][0] > box:
                    continue

                if wv[i][1] > best_value:
                    best_value = wv[i][1]
                    index = i

            if index == -1:
                continue

            is_used[index] = True
            ans += wv[index][1]

        print(ans)


if __name__ == "__main__":
    main()
