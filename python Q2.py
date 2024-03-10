def is_valid_distance(stalls, k, distance):
    horses = 1
    last_stall = stalls[0]
    for stall in stalls[1:]:
        if stall - last_stall >= distance:
            horses += 1
            last_stall = stall
    return horses >= k

def largest_min_distance(stalls, k):
    stalls.sort()
    left, right = 0, stalls[-1] - stalls[0]
    largest_min = -1
    while left <= right:
        mid = (left + right) // 2
        if is_valid_distance(stalls, k, mid):
            largest_min = mid
            left = mid + 1
        else:
            right = mid - 1
    return largest_min

# Example usage
stalls = [1, 2, 4, 8, 9]
k = 3
result = largest_min_distance(stalls, k)
print("Largest minimum distance:", result)