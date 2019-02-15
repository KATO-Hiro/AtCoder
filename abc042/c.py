# -*- coding: utf-8 -*-


def main():
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    like_numbers = [i for i in range(10) if i not in d]
    digit_count = len(list(map(str, list(str(n)))))
    digit = [0] * digit_count
    ans = list()

    def dfs(count):
        if count == digit_count:
            return ans.append(int(''.join(map(str, digit))))

        for like_number in like_numbers:
            digit[count] = like_number
            dfs(count + 1)

    dfs(0)

    if max(ans) >= n:
        print(min([a for a in ans if a >= n]))
    else:
        digit_count += 1
        digit = [0] * digit_count
        dfs(0)
        print(min([a for a in ans if a >= n]))


if __name__ == '__main__':
    main()
