# -*- coding: utf-8 -*-


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    ab = list()
    count = 1

    # See:
    # https://www.youtube.com/watch?v=nVSWen0oM38
    for i in range(m):
        ab.append(tuple(map(int, input().split())))

    sorted_ab = sorted(ab, key=lambda x: x[1])
    b = sorted_ab[0][1]

    for i in range(1, m):
        if sorted_ab[i][0] < b <= sorted_ab[i][1]:
            pass
        else:
            b = sorted_ab[i][1]
            count += 1

    print(count)
