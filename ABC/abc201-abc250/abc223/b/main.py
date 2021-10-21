# -*- coding: utf-8 -*-


def main():
    s = input()
    n = len(s)
    candidates = set()
    candidates.add(s)

    for i in range(n):
        t = s[i:] + s[:i]
        candidates.add(t)
    
    for i in range(n, -1, -1):
        t = s[i:] + s[:i]
        candidates.add(t)

    ans = sorted(candidates)

    print(ans[0])
    print(ans[-1])
    

if __name__ == "__main__":
    main()
