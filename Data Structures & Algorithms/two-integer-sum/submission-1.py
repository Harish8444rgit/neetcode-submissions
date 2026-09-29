class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        alreday_exist={}
        for i in range(len(nums)):
            if alreday_exist.get(target-nums[i]) is not None:
                return [alreday_exist.get(target-nums[i]),i]
            else:
                alreday_exist[nums[i]]=i
        