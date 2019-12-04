# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = input()
    ts = list()

    # KeyInsight
    # 制約条件の小さいものに着目する
    # 部分列では貪欲的に探索することを検討する
    for i in range(10):
        for j in range(10):
            for k in range(10):
                t = ''
                t += str(i)
                t += str(j)
                t += str(k)

                ts.append(t)

    ans = 0

    for ti in ts:
        pos = 0

        for si in s:
            if si == ti[pos]:
                pos += 1

                if pos == 3:
                    break

        if pos == 3:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
