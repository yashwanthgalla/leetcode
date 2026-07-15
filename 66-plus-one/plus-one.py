class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits)))
        num = num+1
        arr = [int(x) for x in str(num)]
        return arr
