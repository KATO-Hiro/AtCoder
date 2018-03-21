'''input
5
12 13 1
44 17 17
66 4096 64
12 13 1

4174
4174
4174
25
0

3
6 5 1
1 10 1

12
11
0

4
12 24 6
52 16 4
99 2 2

187
167
101
0

4
12 13 1
44 17 17
66 4096 64

4162
4162
4162
0

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    station_count = int(input())
    c, s, f = list(), list(), list()

    # HACK: More smarter.
    for _ in range(station_count - 1):
        line = list(map(int, input().split()))
        c.append(line[0])
        s.append(line[1])
        f.append(line[2])

    for i in range(station_count):
        elapsed_time = 0

        for j in range(i, station_count - 1):
            if elapsed_time < s[j]:
                elapsed_time = s[j]
            elif (elapsed_time % f[j]) == 0:
                pass
            else:
                elapsed_time = elapsed_time + f[j] - (elapsed_time % f[j])

            elapsed_time += c[j]

        print(elapsed_time)

    # total_elapsed_times = list()

    # # HACK: More smarter.
    # for i in range(station_count):
    #     if i < station_count - 1:
    #         total_elapsed_times.append(s[i])
    #     else:
    #         total_elapsed_times.append(0)

    # for j in range(station_count - 1):

    #     for k in range(j, station_count - 1):
    #         if total_elapsed_times[j] < s[k]:
    #             total_elapsed_times[j] = s[k]
    #         elif total_elapsed_times[j] % f[j] == 0:
    #             pass
    #         else:
    #             total_elapsed_times[j] += f[k] - (total_elapsed_times[j] % f[k])

    #         total_elapsed_times[j] += c[k]

    # for total_elapsed_time in total_elapsed_times:
    #     print(total_elapsed_time)
