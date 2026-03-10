# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    t = input().rstrip()
    s2 = s.replace("A", "")
    t2 = t.replace("A", "")

    if s2 != t2:
        print(-1)
        exit()

    def count_a(u):
        counts = []
        count = 0

        for ui in u:
            if ui == "A":
                count += 1
            else:
                counts.append(count)
                count = 0

        counts.append(count)

        return counts

    ans = 0

    for si, ti in zip(count_a(s), count_a(t)):
        ans += abs(si - ti)

    print(ans)


if __name__ == "__main__":
    main()
