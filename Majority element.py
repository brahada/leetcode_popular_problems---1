class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d=Counter(nums)
        key_list = list(d.keys()) 
        val_list = list(d.values()) 
        ma=max(val_list)
        return (key_list[val_list.index(ma)])
        
