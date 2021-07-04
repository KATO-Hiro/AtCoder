# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    k = 0

    # 条件を満たすかどうかを判定
    while k * (k - 1) < 2 * n:
        k += 1
    
    if k * (k - 1) != 2 * n:
        print("No")
        exit()
    else:
        print("Yes")
        print(k)
    
    # 部分集合を生成
    i = 1
    numbers = list()
    
    for ki in range(1, k):
        number = list()

        while i <= (ki * (ki + 1) // 2):
            number.append(i)
            i += 1
        
        numbers.append(number)
    
    # 部分集合を列挙
    for i in range(k - 1):
        ans = numbers[i]

        j = i + 1

        while j < k - 1:
            ans.append(numbers[j][i])
            j += 1
        
        print(len(ans), *ans)
    
    ans = [ni[index] for index, ni in enumerate(numbers)]
    print(len(ans), *ans)


if __name__ == "__main__":
    main()
