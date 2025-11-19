class Solution:
    def fib(self, n: int) -> int:
        idx = 2
        sum = 1
        preceding = [0,1]

        if n == 0:
            return 0
        if n ==1:
            return 1
        
        while idx <= n:
            sum = preceding[idx-1] + preceding[idx-2]
            preceding.append(sum)
            idx += 1
        
        return sum
        