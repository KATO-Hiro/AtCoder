# -*- coding: utf-8 -*-


class Prime:
    """Represents a snippet for prime numbers."""

    def __init__(self, number):
        self.number = number
        self._values = []

    def generate(self) -> list:
        if self._values:
            return self._values

        is_met = [True for _ in range(self.number + 1)]
        is_met[0] = False
        is_met[1] = False

        for i in range(2, self.number + 1):
            if is_met[i]:
                self._values.append(i)

                for j in range(2 * i, self.number + 1, i):
                    is_met[j] = False
        return self._values


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    p = Prime(10**6 + 1)
    ps = p.generate()
    m = len(ps)
    ans = 0

    for i in range(m - 2):
        a = ps[i]
        a2 = a**2

        if a2 > n:
            break

        for k in range(i + 2, m):
            c = ps[k]
            c2 = c**2

            if a2 * c2 > n:
                break

            for j in range(i + 1, m - 1):
                b = ps[j]

                if b >= c:
                    continue

                if a2 * b > n:
                    break

                if a2 * b * c2 > n:
                    break

                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
