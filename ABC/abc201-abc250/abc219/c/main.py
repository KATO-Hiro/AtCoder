# -*- coding: utf-8 -*-


def main():
    from string import ascii_lowercase

    x = input()
    n = int(input())
    d = {xi: ascii_lowercase[index] for index, xi in enumerate(x)}
    t = list()

    for _ in range(n):
        s = input()
        u = ""

        for si in s:
            u += d[si]
        t.append((u, s))
        
    for _, ans in sorted(t):
        print(ans)


if __name__ == "__main__":
    main()
