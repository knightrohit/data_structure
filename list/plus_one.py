"""Given a non-empty array of digits representing a non-negative integer, plus one to the integer
Input: [1,2,3]
Output: [1,2,4]
""""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if not digits:
            return []        

        num = 0
        out =[]
        i = 0
        while digits:
            num += digits.pop()*(10**i)
            i += 1
            
        num += 1
        
        while num > 0:
            out.append(num%10)
            num = num // 10
            
        return out[::-1]