# -*- coding: utf-8 -*-


def main():
    s_dash = input()
    t = input()
    s_count = len(s_dash)
    t_count = len(t)
    ans = list()

    for i in range(s_count - t_count + 1):
        si = s_dash[i:i + t_count]

        count = 0

        for sj, tj in zip(si, t):
            if sj == '?':
                count += 1
            elif sj == tj:
                count += 1

        if count == t_count:
            s = s_dash[:i] + t + s_dash[i + count:]
            s = s.replace('?', 'a')
            ans.append(s)

    if len(ans) > 0:
        print(sorted(ans)[0])
    else:
        print('UNRESTORABLE')


if __name__ == '__main__':
    main()
