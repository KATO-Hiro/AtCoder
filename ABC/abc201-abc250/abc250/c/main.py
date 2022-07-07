# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    balls = [i for i in range(n)]
    pos = [balls[i] for i in range(n)]

    for i in range(q):
        xi = int(input())
        xi -= 1

        i = pos[xi]
        j = i + 1

        # 右端
        if j == n:
            j = i - 1

        yi = balls[j]

        balls[i], balls[j] = balls[j], balls[i]
        pos[xi], pos[yi] = pos[yi], pos[xi]

    ans = list()

    for ball in balls:
        ans.append(ball + 1)

    print(*ans)


if __name__ == "__main__":
    main()
