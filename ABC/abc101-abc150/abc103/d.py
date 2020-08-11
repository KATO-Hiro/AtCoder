# -*- coding: utf-8 -*-


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    ab = sorted([tuple(map(int, input().split())) for _ in range(m)],
                key=lambda x: x[1])
    count = 1

    # See:
    # https://www.youtube.com/watch?v=nVSWen0oM38
    b = ab[0][1]

    for i in range(1, m):
        if ab[i][0] >= b:
            b = ab[i][1]
            count += 1

    print(count)
