class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        
        out = []        
        if not A:
            return A        
        if len(A) == 1:
            return A        
        p1 = 0        
        for i in range(len(A)):
            if A[i] < 0:
                p1 += 1
            A[i] = A[i]**2
            
        p2 = p1
        p1= p1 - 1
        while p2 < len(A) and p1 >=0:
            if A[p1] > A[p2]:
                out.append(A[p2])
                p2 += 1
                
            elif A[p1] == A[p2]:
                out.append(A[p1])
                out.append(A[p2])
                p1 -= 1
                p2 += 1
                
            else:
                out.append(A[p1])
                p1 -= 1
        while p2 < len(A):
            out.append(A[p2])
            p2 += 1
        while p1 >=0 :
            out.append(A[p1])
            p1 -= 1
              
        return out