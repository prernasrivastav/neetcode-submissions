class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Convert array to a set (removes all duplicates)
        # Then compare the size of the set with the original array
        # If set is smaller, duplicates must have existed
        return len(set(nums)) < len(nums)