
# Non-Divisible Subset

This Python script solves the "Non-Divisible Subset" problem, where the goal is to find the largest subset of a given set of integers such that the sum of any two numbers in the subset is not divisible by a given integer `k`.

## Problem Description

Given a set of integers, `S`, and an integer, `k`, find the largest subset, `S'`, of `S` where the sum of any two numbers in `S'` is not evenly divisible by `k`.

### Input

- A list of integers `S` representing the scores in each game.
- An integer `k`, the divisor.

### Output

- The size of the largest possible subset `S'` where no two numbers in the subset sum to a multiple of `k`.

## Implementation

The `nonDivisibleSubset` function takes a divisor `k` and a list of integers `S` as input and returns the size of the largest subset where no two elements sum to a multiple of `k`.

### Example

```python
def nonDivisibleSubset(k, S):
    # Step 1: Calculate remainder frequencies
    remainder_count = [0] * k
    for num in S:
        remainder_count[num % k] += 1
    
    # Step 2: Initialize the subset size with the count of remainder 0 (if any)
    max_subset_size = min(remainder_count[0], 1)
    
    # Step 3: Handle the rest of the remainders
    for r in range(1, (k // 2) + 1):
        if r != k - r:
            max_subset_size += max(remainder_count[r], remainder_count[k - r])
        else:
            # Special case when remainder is exactly half of k
            max_subset_size += min(remainder_count[r], 1)
    
    return max_subset_size

# Example usage:
n, k = map(int, input().split())
S = list(map(int, input().split()))
result = nonDivisibleSubset(k, S)
print(result)
```

### Iteration Table

Given the example scores `[1, 7, 2, 4]` and `k = 3`, the function works as follows:

| Number | Remainder when divided by 3 | remainder_count array after this number |
|--------|-----------------------------|-----------------------------------------|
|   1    |             1               | [0, 1, 0]                               |
|   7    |             1               | [0, 2, 0]                               |
|   2    |             2               | [0, 2, 1]                               |
|   4    |             1               | [0, 3, 1]                               |

Final `remainder_count` array: `[0, 3, 1]`

### Explanation of Steps

1. **Remainder Calculation:**
   - Calculate the remainder of each number in the set when divided by `k`.
   - Count the frequency of each remainder.

2. **Subset Construction:**
   - If there is a remainder `0`, you can include only one element with this remainder in the subset.
   - For other remainders, pick the maximum count between remainder `r` and `k-r`.
   - If `k` is even, include only one element with a remainder of `k/2`.

### Usage

To use this function, input your scores and divisor, then call the `nonDivisibleSubset` function:

```python
S = [1, 7, 2, 4]
k = 3
result = nonDivisibleSubset(k, S)
print("Size of the largest non-divisible subset:", result)
```

### Output

For the example input above, the output will be:

```
Size of the largest non-divisible subset: 3
```

## License

This project is open-source and available under the MIT License.
