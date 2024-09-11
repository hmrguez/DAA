def brute_force_numbness(n: int, a: [int]) -> int:
    max_numbness = 0

    # Iterate over all possible subarrays
    for l in range(n):
        for r in range(l, n):
            # Calculate max and XOR for the subarray a[l...r]
            subarray_max = a[l]
            subarray_xor = 0

            for i in range(l, r + 1):
                subarray_max = max(subarray_max, a[i])
                subarray_xor ^= a[i]

            # Calculate numbness for this subarray
            numbness = subarray_max ^ subarray_xor

            # Update the maximum numbness
            max_numbness = max(max_numbness, numbness)

    return max_numbness


if __name__ == "__main__":
    test_cases = int(input())

    for _ in range(test_cases):
        n = int(input())
        a = [int(x) for x in input().split()]

        ans = brute_force_numbness(n, a)
        print(ans)
