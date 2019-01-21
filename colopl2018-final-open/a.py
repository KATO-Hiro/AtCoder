# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = list(input())
    s_count = len(s)
    attack_count = [0 for _ in range(s_count)]

    if len(set(s)) == 1:
        if s[0] == 'A':
            n *= s_count
            print(n * (n + 1) // 2)
            exit()

    if s[0] == 'A':
        attack_count[0] = 1

    for i in range(1, s_count):
        if s[i] == 'A':
            attack_count[i] = attack_count[i - 1] + 1

    ans = sum(attack_count) * n

    if s[0] == 'A' and s[-1] == 'A':
        count = 0

        for si in s:
            if si == 'A':
                count += 1
            else:
                break

        ans += (attack_count[-1] * count) * (n - 1)

    print(ans)


if __name__ == '__main__':
    main()
