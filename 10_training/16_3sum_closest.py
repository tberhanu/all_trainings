
def closest_3sum(nums, target):
    """Runtime: 148 ms, faster than 50.53% of Python3 online submissions for 3Sum Closest.
"""
    nums = sorted(nums)
    r = nums[0] + nums[1] + nums[len(nums) - 1]
    for i in range(len(nums) - 2):
        j, k = i + 1, len(nums) - 1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]

            if sum == target:
                return sum
            if abs(sum - target) < abs(r - target):
                r = sum

            if sum < target:
                j += 1

            if sum > target:
                k -= 1

    return r


nums = [-1, 2, 1, -4]
target = 1
print(closest_3sum(nums, target))

nums = [1, 4, 5, 3, 8, -4]
target = 3
print(closest_3sum(nums, target))
nums = [1, 4, 5, 3, 8, -4]
target = 7
print(closest_3sum(nums, target))
