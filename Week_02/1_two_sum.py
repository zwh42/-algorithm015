class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        v_dict = {}
        for i, v in enumerate(nums):
           v_dict[v] = i
            
        for i, v in enumerate(nums):
            complement_v = target - v
            if complement_v in v_dict and v_dict[complement_v] != i:
                return [i, v_dict[complement_v]]

        return []