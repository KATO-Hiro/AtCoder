def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [ai - bi for ai, bi in zip(a, b)]
    w = []
    lower, upper = 1, 10**18

    for ci in c:
        if ci > 0:
            w.append(upper)
        else:
            w.append(lower)

    sum_a, sum_b = 0, 0

    for ai, bi, wi in zip(a, b, w):
        sum_a += ai * wi
        sum_b += bi * wi

    if sum_a > sum_b:
        print("Yes")
        print(*w)
    else:
        print("No")


if __name__ == "__main__":
    main()
