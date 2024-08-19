""" Problem
Sparkle gives you two arrays 𝑎 and 𝑏 of length 𝑛. Initially, your score is 0. In one operation, you can choose an integer 𝑖and add 𝑎𝑖 to your score. Then, you must set 𝑎𝑖 = max(0,𝑎𝑖−𝑏𝑖).

You only have time to perform 𝑘 operations before Sparkle sets off a nuclear bomb! What is the maximum score you can acquire after 𝑘 operations?
"""


def solve(a, b, n, k):
    low, top = 0, max(a) + 1
    while top - low > 1:
        mid = (low + top) // 2

        sum_val = 0
        for i in range(n):
            if a[i] >= mid:
                sum_val += (a[i] - mid) // b[i] + 1

        if sum_val >= k:
            low = mid
        else:
            top = mid

    ans = 0
    s = 0

    for i in range(n):
        if a[i] >= low:
            t = (a[i] - low) // b[i] + 1
            ans += t * a[i] - t * (t - 1) // 2 * b[i]
            s += t

    ans -= low * (s - k)

    return ans


if __name__ == "__main__":
    # n, k = 3, 4
    # a = [5, 6, 7]
    # b = [2, 3, 4]

    # 5 9
    # 32 52 68 64 14
    # 18 14 53 24 8

    # n, k = 5, 9
    # a = [32, 52, 68, 64, 14]
    # b = [18, 14, 53, 24, 8]

    # 5 1000
    # 1 2 3 4 5
    # 5 4 3 2 1

    # n, k = 5, 1000
    # a = [1, 2, 3, 4, 5]
    # b = [5, 4, 3, 2, 1]

    n, k = 10, 6
    a = [3, 3, 5, 10, 6, 8, 6, 8, 7, 7]
    b = [6, 1, 7, 4, 1, 1, 8, 9, 3, 1]

    print(solve(a, b, n, k))
