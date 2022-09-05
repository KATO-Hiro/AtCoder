# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    k = int(input())

    if k % 2 == 0:
        print(-1)
        exit()

    values = [0] * (k + 1)
    value = 7
    value %= k

    # modの世界で考える
    for i in range(k + 1):
        values[i] = value
        value *= 10
        value += 7
        value %= k
    
    for i, value in enumerate(values, 1):
        if value == 0:
            print(i)
            exit()

    print(-1)


if __name__ == "__main__":
    main()
