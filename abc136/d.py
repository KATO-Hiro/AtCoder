# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate

    s = input()
    children_count = list()
    pos = 'R'
    r_count = 0
    l_count = 0

    if s[0] == 'L':
        children_count.append(0)
        pos = 'L'

    for si in s:
        if pos == 'R':
            if si == 'R':
                r_count += 1
            else:
                children_count.append(r_count)
                r_count = 0
                pos = 'L'
                l_count += 1
        else:
            if si == 'L':
                l_count += 1
            else:
                children_count.append(l_count)
                l_count = 0
                pos = 'R'
                r_count += 1

    if r_count > 0:
        children_count.append(r_count)

    if l_count > 0:
        children_count.append(l_count)

    if s[-1] == 'R':
        children_count.append(0)

    ans = [0 for _ in range(len(s))]

    summed = list(accumulate(children_count))

    for i in range(len(summed) // 2):
        ri_count = children_count[2 * i]
        li_count = children_count[2 * i + 1]

        if (ri_count + li_count) % 2 == 0:
            ans[summed[2 * i] - 1] = (ri_count + li_count) // 2
            ans[summed[2 * i]] = (ri_count + li_count) // 2
        else:
            if ri_count > li_count:
                ans[summed[2 * i] - 1] = ri_count
                ans[summed[2 * i]] = li_count
            else:
                ans[summed[2 * i] - 1] = li_count
                ans[summed[2 * i]] = ri_count

    print(' '.join(map(str,ans)))


if __name__ == '__main__':
    main()
