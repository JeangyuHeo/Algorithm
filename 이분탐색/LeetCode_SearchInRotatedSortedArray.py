class Solution:
    def search(self, nums: List[int], target: int) -> int:
        answer = -1
        
        for idx, num in enumerate(nums):
            if num == target:
                answer = idx
                break

        return answer