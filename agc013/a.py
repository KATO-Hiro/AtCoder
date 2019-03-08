# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [a[0]]
    ans = 1

    for i, j in zip(a, a[1:]):
        if i != j:
            b.append(j)

    m = len(b)
    i = 0
    j = 1

    while i + 1 < m:
        while j + 1 < m:
            if (b[i + 1] - b[i]) * (b[j + 1] - b[j]) < 0:
                ans += 1
                i = j + 1
            j += 1

        i += 1

    print(ans)


if __name__ == '__main__':
    main()
