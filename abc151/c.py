# -*- coding: utf-8 -*-


def main():
    n, m = map(int, input().split())
    ac_count = [0 for _ in range(n)]
    wa_count = [0 for _ in range(n)]

    for i in range(m):
        pi, si = input().split()
        pi = int(pi)
        pi -= 1

        if si == 'WA':
            if ac_count[pi] == 0:
                wa_count[pi] += 1
        else:
            if ac_count[pi] == 0:
                ac_count[pi] = 1

    total_ac = sum(ac_count)
    total_wa = 0

    for ac, wa in zip(ac_count, wa_count):
        if ac == 1:
            total_wa += wa

    print(total_ac, total_wa)


if __name__ == '__main__':
    main()
