def four_sum(nums, target):
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 3):
        # Avoid duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n - 2):
            # Avoid duplicates
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left = j + 1
            right = n - 1

            while left < right:
                curr_sum = nums[i] + nums[j] + nums[left] + nums[right]

                if curr_sum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Avoid duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1

    return result

# Example usage
nums = [1, 0, -1, 0, -2, 2]
target = 0
result = four_sum(nums, target)
print(result)
