from itertools import product
import heapq


def solve(a: [int], b: [int], n: int, k: int) -> int:
    heap = []
    for i in range(n):
        heapq.heappush(heap, (-a[i], i))

    score = 0
    #
    # Perform k operations
    for _ in range(k):
        poppedA, i = heapq.heappop(heap)

        # Add the value to the score
        score -= poppedA

        # Update a[i]
        a[i] = max(0, a[i] - b[i])

        # Update the heap
        heapq.heappush(heap, (-a[i], i))

    return score


if __name__ == "__main__":
    n, k = 10, 6
    a = [3, 3, 5, 10, 6, 8, 6, 8, 7, 7]
    b = [6, 1, 7, 4, 1, 1, 8, 9, 3, 1]

    print(solve(a, b, n, k))
