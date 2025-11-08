class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for i in nums:
            res[i] = 1 + res.get(i,0)
        sorted_items = sorted(res.items(), key=lambda x: x[1], reverse=True)
        return [num for num, freq in sorted_items[:k]]