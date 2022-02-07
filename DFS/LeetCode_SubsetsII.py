from itertools import combinations

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]
        subset_size = 1
        length = len(nums)
        
        while subset_size <= length:
            for item in combinations(nums, subset_size):
                tmp = sorted(list(item))
                if tmp not in answer:
                    answer.append(tmp)
            subset_size+=1

        return answer