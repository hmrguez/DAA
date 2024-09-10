MOD = 998244353


def solve(n: int, s: [str]) -> int:
    """Divide and conquer solution"""
    s = " " + s

    def solve_rec(x: int) -> (int, str):

        l = 2 * x
        r = 2 * x + 1

        if l >= len(s):
            return 1, s[x]

        left_pre, left_small = solve_rec(l)
        right_pre, right_small = solve_rec(r)

        t = min(s[x] + left_small + right_small, s[x] + right_small + left_small)

        if left_small == right_small:
            return (left_pre * right_pre) % MOD, t
        else:
            return 2 * left_pre * right_pre % MOD, t

    return solve_rec(1)[0]


if __name__ == "__main__":
    n = 2
    s = "AAA"
    print(solve(n, s))
