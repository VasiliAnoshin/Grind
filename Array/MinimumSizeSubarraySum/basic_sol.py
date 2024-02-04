class Solution:
    def minSubArrayLen(self, target: int, nums:list[int]) -> int:
        res = float('inf')
        i=k=0
        j=len(nums)
        tmp=0
        while k<j:
            if tmp<target:
                tmp+=nums[k]
                k+=1
            if tmp>=target:
                while tmp>=target:
                    res = min(k-i, res)
                    tmp-=nums[i]
                    i+=1
        return 0 if res == float('inf') else res