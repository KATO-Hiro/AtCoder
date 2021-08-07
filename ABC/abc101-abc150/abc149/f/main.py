# -*- coding: utf-8 -*-


def main():
    n, m = map(int, input().split())
    s = list(input())[::-1]
    right = 0
    ans = list()
    inf = float("inf")

    while right < n:
        candidate = inf

        for i in range(1, m + 1):
            pos = right + i

            if pos < n + 1 and s[pos] == "0":
                candidate = i
        
        if candidate == inf:
            print("-1")
            exit()
        else:
            ans.append(candidate)
        
        right += candidate
    
    print(' '.join(map(str, ans[::-1])))


if __name__ == "__main__":
    main()
