from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]
        subset_size = 1
        length = len(nums)
        
        while subset_size <= length:
            for item in combinations(nums, subset_size):
                answer.append(list(item))
            subset_size+=1

        return answer