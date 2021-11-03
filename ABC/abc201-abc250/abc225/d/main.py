# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    m = 10 ** 5 + 1
    front = [-1] * m
    back = [-1] * m

    for _ in range(q):
        query = list(map(int, input().split()))
        ci = query[0]

        if ci == 3:
            x = query[1]
            x -= 1

            while front[x] != -1:
                x = front[x]
            
            ans = [x + 1]
            
            while back[x] != -1:
                x = back[x]
                ans.append(x + 1)
            
            print(len(ans), *ans)
        else:
            x, y = query[1], query[2]
            x -= 1
            y -= 1

            if ci == 1:
                back[x] = y
                front[y] = x
            else:
                back[x] = -1
                front[y] = -1


if __name__ == "__main__":
    main()
