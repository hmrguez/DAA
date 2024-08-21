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

    # if left_small < right_small:
    #     return (left_pre * right_pre) % MOD, left_small + s[x] + right_small
    # else:
    #     return (2 * left_pre * right_pre) % MOD, right_small + s[x] + left_small


# def solve_rec(l: int, r: int, i: int) -> (int, str):
#     """Recursive helper function"""
#
#
#
#
#     if l == r:
#         return 1, s[l]
#
#     m = (l + r) // 2
#     left = solve_rec(l, m, i + 1)
#     right = solve_rec(m + 1, r, i + 1)
#
#     if left[1] < right[1]:
#         return (left[0] * right[0]) % MOD, left[1] + right[1]
#     else:
#         return (2 * left[0] * right[0]) % MOD, right[1] + left[1]

# return solve_rec(0, n - 1, 0)[0]

# def solve(n, s):
#     # Initialize dp array
#     dp = [0] * (2 * n)
#     # Initialize minimal lexicographical string for each node
#     t = [""] * (2 * n)
#
#     # Fill the dp and t arrays for leaf nodes
#     for i in range(n - 1, 2 * n - 1):
#         dp[i] = 1
#         t[i] = s[i]
#
#     # Fill dp and t arrays for internal nodes
#     for i in range(n - 2, -1, -1):
#         left_child = 2 * i + 1
#         right_child = 2 * i + 2
#         # Calculate the lexicographically smallest preorder string
#         t1 = t[left_child] + s[i] + t[right_child]
#         t2 = t[right_child] + s[i] + t[left_child]
#         t[i] = min(t1, t2)
#
#         # If the preorder strings are the same
#         if t1 == t2:
#             dp[i] = dp[left_child] * dp[right_child] % MOD
#         else:
#             dp[i] = 2 * dp[left_child] * dp[right_child] % MOD
#
#     # The answer is the dp value at the root (index 0)
#     return dp[0]
#
#
# # Example Usage:
# B AA AAAA AABBABAB

n = 2
s = "AAA"
print(solve(n, s))  # Output: 2
