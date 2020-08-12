# -*- coding: utf-8 -*-


# Dynamic programming Python implementation of LIS problem

# lis returns length of the logest increasing subsequence
# in arr of size n
def lis(arr):
    n = len(arr)

    # Declare the list (array) for LIS and initialize LIS
    # values for all indexes
    lis = [1] * n

    # Compute optimized LIS values in bottom up manner
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    # Pick maximum of all LIS values
    return max(lis)


def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(lis(a))


if __name__ == '__main__':
    main()
