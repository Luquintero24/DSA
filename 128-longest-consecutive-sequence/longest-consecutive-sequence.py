class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums = set(nums)
        longest = 0

        for n in setnums:
            if (n-1) not in setnums:
                length = 0 
                while (n+length) in setnums:
                    length += 1
                    longest = max(length, longest)
        return longest
        