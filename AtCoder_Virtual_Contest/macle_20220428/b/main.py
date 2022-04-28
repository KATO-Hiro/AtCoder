# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = list(input().rstrip())
    w_count = [0] * (n + 1)
    e_count = [0] * (n + 1)

    for index, si in enumerate(s, 1):
        if si == "E":
            e_count[index] = 1
        else:
            w_count[index] = 1
    
    e_count = list(accumulate(e_count))
    w_count= list(accumulate(w_count))
    ans = float("inf")

    for i in range(1, n + 1):
        wi = w_count[i - 1]
        ei = e_count[n] - e_count[i]
        summed = wi + ei
        ans = min(ans, summed)
    
    print(ans)


if __name__ == "__main__":
    main()
