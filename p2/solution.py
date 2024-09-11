class Trie:
    def __init__(self):
        self.child = [None, None]


def insert(trie: Trie, x: int) -> None:
    temp = trie
    for i in range(30, -1, -1):
        curr = (x >> i) & 1
        if temp.child[curr] is None:
            temp.child[curr] = Trie()
        temp = temp.child[curr]


def find_greatest(trie: Trie, x: int) -> int:
    res = 0
    temp = trie
    for i in range(30, -1, -1):
        curr = (x >> i) & 1
        if temp.child[curr ^ 1]:
            res ^= (1 << i)
            temp = temp.child[curr ^ 1]
        else:
            temp = temp.child[curr]
    return res


def solve(n: int, a: [int]) -> int:
    # Initialize Trie and prexor
    t = [None] * (n + 2)
    prexor = [0] * (n + 1)
    for i in range(1, n + 1):
        t[i] = Trie()
        insert(t[i], prexor[i - 1])
        prexor[i] = prexor[i - 1] ^ a[i]

    t[n + 1] = Trie()
    insert(t[n + 1], prexor[n])

    # Sort elements by value and store their original index
    asc = [(a[i], i) for i in range(1, n + 1)]
    asc.sort()

    # Find the left and right boundaries for each element
    left = [0] * (n + 1)
    right = [0] * (n + 1)
    s = []
    for i in range(1, n + 1):
        while s and a[i] >= a[s[-1]]:
            s.pop()
        left[i] = 0 if not s else s[-1]
        s.append(i)

    s.clear()
    for i in range(n, 0, -1):
        while s and a[i] > a[s[-1]]:
            s.pop()
        right[i] = n + 1 if not s else s[-1]
        s.append(i)

    # Calculate the maximum result
    ans = 0
    for value, x in asc:
        r = right[x] - 1
        l = left[x] + 1
        if x - l < r - x:
            for j in range(l - 1, x):
                ans = max(ans, find_greatest(t[x + 1], prexor[j] ^ a[x]))
            t[l] = t[x + 1]
            for j in range(l - 1, x):
                insert(t[l], prexor[j])
        else:
            for j in range(x, r + 1):
                ans = max(ans, find_greatest(t[l], prexor[j] ^ a[x]))
            for j in range(x, r + 1):
                insert(t[l], prexor[j])

    return ans


def main():
    test_cases = int(input())

    for _ in range(test_cases):
        n = int(input())
        a = [0] + [int(x) for x in input().split()]

        ans = solve(n, a)
        print(ans)


if __name__ == "__main__":
    main()
