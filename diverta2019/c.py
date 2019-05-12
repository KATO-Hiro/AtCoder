# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = [input() for _ in range(n)]
    ans = 0
    back_a_count = 0
    front_b_count = 0
    front_b_back_a_count = 0

    for si in s:
        if si[0] == 'B':
            front_b_count += 1
        if si[-1] == 'A':
            back_a_count += 1
        if si[0] == 'B' and si[-1] == 'A':
            front_b_back_a_count += 1

        for j in range(len(si) - 1):
            if (si[j] == 'A' and si[j + 1] == 'B'):
                ans += 1

    ans += min(back_a_count, front_b_count)

    # See:
    # https://www.youtube.com/watch?v=AQOZYEk54rw
    if front_b_count == back_a_count == front_b_back_a_count:
        if front_b_back_a_count > 0:
            ans -= 1

    print(ans)


if __name__ == '__main__':
    main()
