def ceil(a: int, b: int) -> int:
    assert b != 0

    return (a + b - 1) // b


def main():
    import sys

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0

    for ai in a:
        count += ceil(ai, k)

    ans = max(0, count - m)
    print(ans)


if __name__ == "__main__":
    main()
