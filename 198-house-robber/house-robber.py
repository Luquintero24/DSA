class Solution:
    def rob(self, nums: List[int]) -> int:
        # n = len(nums)
        #edge case: 
        # if n == 1:
        #     return nums[0]
        # #create a dp array to store previous values
        # dp = [0]*n
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])
        # #loop thru the rest of the houses
        # for i in range(2, n):
        #     dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        #     # 2 ways: (1) take from previous house (not current one)
        #             # (2) take from priovious prvious house and this current one
        #             # and then compare which one has more money
        # return dp[-1]
        prev1, prev2 = 0, 0
        for num in nums:
            cur = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = cur
        return prev1