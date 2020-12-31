class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        max = nums[-1]
        defaultValue: int = max + 1
        i: int = 1
        j: int = 1
        count: int = 1
        extraLength: int = 0
        length: int = len(nums)
        while i < length:
            if nums[i] == nums[i-j]:
                count += 1
                if count > 2:
                    nums[i] = defaultValue
                    extraLength += 1
                    j += 1
            else:
                count = 1
                j = 1
            i += 1
        nums.sort()
        return length - extraLength
