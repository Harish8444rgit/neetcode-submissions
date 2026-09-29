class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use optimal solution for set size and array size 
        # which reduce the code only 
        distinct_nums=set(nums)
        return not len(distinct_nums)==len(nums)
        