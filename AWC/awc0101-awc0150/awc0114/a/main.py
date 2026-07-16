# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    xp = [tuple(map(int, input().split())) for _ in range(n)]
    ans = 0

    for r in range(100 + 1):
        candidate = -(r**2)

        for xi, pi in xp:
            if not (-r <= xi <= r):
                continue

            candidate += pi

        ans = max(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()
