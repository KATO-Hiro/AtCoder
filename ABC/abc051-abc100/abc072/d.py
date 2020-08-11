# -*- coding: utf-8 -*-


def main():
    n = int(input())
    p = list(map(int, input().split()))
    is_same = [False for _ in range(n)]
    ans = 0

    for index, pi in enumerate(p, 1):
        diff = pi - index

        if diff == 0:
            is_same[index - 1] = True

    i = 0

    while i < n:
        if i == n - 1 and is_same[i]:
            ans += 1
            break

        if is_same[i] and is_same[i + 1]:
            i += 2
            ans += 1
        elif is_same[i] and not is_same[i + 1]:
            i += 2
            ans += 1
        else:
            i += 1

    print(ans)


if __name__ == '__main__':
    main()
