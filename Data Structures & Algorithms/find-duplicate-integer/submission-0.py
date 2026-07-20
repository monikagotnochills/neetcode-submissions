class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        Slow , Fast = 0,0
        while True:
            Slow = nums[Slow]
            Fast = nums[nums[Fast]]
            if Slow == Fast:
                break 
        Slow2 = 0         
        while True:
            Slow = nums[Slow]
            Slow2 = nums[Slow2]
            if Slow == Slow2:
                return Slow      
