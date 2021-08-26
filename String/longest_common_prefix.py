"""
Time Complexity = O(N^2)
Space Complexity = O(N)
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ''
        
        min_word_size = min(len(_) for _ in strs)
        i = 0
        out = []
        match = True
        while i < min_word_size and match:
            word = None
            for c in range(len(strs)):
                if not word:
                    word = strs[c][i]
                    continue
                if strs[c][i] != word:
                    match = False
                    break
            else:
                out.append(word)
                i += 1
        return  ''.join(out)