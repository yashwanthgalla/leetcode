class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        sum1=1
        sum2=1
        nums.sort()
        sum1= nums[-1]*nums[-2]*nums[-3]
        sum2= nums[0]*nums[1]*nums[-1]
        return max(sum1,sum2)