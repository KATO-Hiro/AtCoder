# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = sorted(a)
    ans = [0] * n

    for i in range(k):
        tmp = a[i::k]
        index = [i]

        for j in range(i + k, n, k):
            index.append(j)
        
        tmp = sorted(tmp)

        for id, t in zip(index, tmp):
            ans[id] = t
    
    if ans == b:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
