""" https://leetcode.com/problems/wiggle-subsequence/
"""
def wiggleMaxLength(self, nums):

    if len(nums) <= 2:
        return len(nums)

        state = 0
        counter = 1

        for i in range(1, len(nums)):
            diff = (nums[i] - nums[i-1])

            if diff * state <= 0 and diff != 0:
                counter += 1
                state = diff

        return counter
