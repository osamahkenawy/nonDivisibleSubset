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


# Iteration Table Example:
# Consider S = [1, 7, 2, 4], k = 3

# Step 1: Calculate remainder frequencies
# | Number | Remainder when divided by 3 | remainder_count array after this number |
# |--------|-----------------------------|-----------------------------------------|
# |   1    |             1               | [0, 1, 0]                               |
# |   7    |             1               | [0, 2, 0]                               |
# |   2    |             2               | [0, 2, 1]                               |
# |   4    |             1               | [0, 3, 1]                               |

# Final remainder_count array: [0, 3, 1]

# Step 2: Initialize subset size with remainder 0
# max_subset_size = min(0, 1) = 0

# Step 3: Handle other remainders
# | r | remainder_count[r] | remainder_count[k - r] | max_subset_size | Action                            
# |---|--------------------|-----------------------|-----------------|-----------------------------------|
# | 1 | 3                  | 1                     | 3               | Add max(remainder_count[1], remainder_count[2]) 