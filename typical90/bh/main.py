# -*- coding: utf-8 -*-


from typing import List, Tuple


# See:
# https://qiita.com/python_walker/items/d1e2be789f6e7a0851e5
# https://atcoder.jp/contests/typical90/submissions/23271010
def lis(seq: List) -> Tuple[List[int], List[int]]:
    from bisect import bisect_left

    sub_seq = [seq[0]]
    sub_seq_size = list()

    for i in range(len(seq)):
        if seq[i] > sub_seq[-1]:
            sub_seq.append(seq[i])
        else:
            index = bisect_left(sub_seq, seq[i])
            sub_seq[index] = seq[i]
        
        sub_seq_size.append(len(sub_seq))
        
    return sub_seq_size, sub_seq


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    z = a[::-1]
    c, _ = lis(a)
    d, _ = lis(z)
    ans = 1

    for ci, di in zip(c, d[::-1]):
        ans = max(ans, ci + di - 1) 

    print(ans)


if __name__ == "__main__":
    main()
