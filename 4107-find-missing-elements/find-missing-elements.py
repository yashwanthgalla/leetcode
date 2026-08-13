class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = set(nums)
        a = max(nums)
        b = min(nums)
        c = []
        for i in range(b,a+1):
            if i not in s:
                c.append(i)
        return c