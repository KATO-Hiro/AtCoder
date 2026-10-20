def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: -x[1])
    remain = k
    ans = 0

    for ai, bi in ab:
        need = min(remain, ai)
        remain -= need
        ans += need * bi

    if remain > 0:
        ans = -1

    print(ans)


if __name__ == "__main__":
    main()
