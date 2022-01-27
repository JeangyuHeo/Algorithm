class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        answer = []
        window_size = len(p)
        sentence_size = len(s)
        
        p_list = sorted(list(p))
        s_list = list(s)
        
        for i in range(sentence_size - window_size+1):
            if sorted(s_list[i:i+window_size]) == p_list:
                answer.append(i)
        
        return answer