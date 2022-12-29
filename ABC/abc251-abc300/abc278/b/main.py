# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, m = map(int, input().split())

    for delta in range(2 * 24 * 60 + 10):
        minutes = h * 60 + m + delta
        hi, mi = (minutes // 60) % 24, minutes % 60

        time = list(str(hi).zfill(2) + str(mi).zfill(2))
        time[1], time[2] = time[2], time[1]
        time = ''.join(time)
        hj, mj = int(time[:2]), int(time[2:])

        if 0 <= hj <= 23 and 0 <= mj <= 59:
            print(hi, mi)
            exit()
    

if __name__ == "__main__":
    main()
