def main():
    import sys

    input = sys.stdin.readline

    n, x = map(int, input().split())
    ans = -1

    for _ in range(n):
        ci, ai = map(int, input().split())

        if ci != x:
            continue

        ans = max(ans, ai)

    print(ans)


if __name__ == "__main__":
    main()
