# -*- coding: utf-8 -*-


def main():
    s_dash = input()
    t = input()
    s_dash_count = len(s_dash)
    t_count = len(t)
    ans = list()

    if s_dash_count >= t_count:
        for k in range(s_dash_count - t_count + 1):
            mod_s_dash = s_dash[k:k + t_count]
            count = 0

            for i in range(t_count):
                if mod_s_dash[i] == t[i]:
                    count += 1
                elif mod_s_dash[i] == '?':
                    count += 1

            if count == t_count:
                s = s_dash[:k] + t + s_dash[k + t_count:]
                s = s.replace('?', 'a')
                ans.append(s)

        if len(ans) == 0:
            print('UNRESTORABLE')
        else:
            print(sorted(ans)[0])

    else:
        print('UNRESTORABLE')


if __name__ == '__main__':
    main()
