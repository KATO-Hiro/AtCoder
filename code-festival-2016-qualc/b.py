# -*- coding: utf-8 -*-


def main():
    k, t = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    pre_pos = 0
    a[pre_pos] -= 1
    ans = 0

    for i in range(1, k):
        for j in range(t):
            if pre_pos != j and a[j] > 0:
                a[j] -= 1
                pre_pos = j
                break
        else:
            ans += 1
        print('after', a)
        # print('pre', a)

    print(ans)


if __name__ == '__main__':
    main()
