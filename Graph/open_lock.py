"""
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".

Time Complexity : (Size of lock)^no_of_digit * no_of_digit + (dead set conversion)
Space Compexity : (Size of lock)^no_of_digit + (dead set conversion)
"""

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if not target:
            return None
        
        visited = {'0000'}
        queue = deque()
        queue.append(('0000', 0))
        dead_set = set(deadends)
        depth = 0
        
        
        def generate_nodes(node):
            for i in range(4):
                for d in [-1, 1]:
                    x = int(node[i])
                    temp = (x + d) % 10
                    yield node[:i] + str(temp) + node[i+1 : ]               
            
        
                
        while queue:
            node, depth = queue.popleft()
            
            if node == target: return depth            
            if node in dead_set: continue
                
            for child in generate_nodes(node):
                if child in visited:
                    continue
                
                visited.add(child)
                queue.append((child, depth + 1))
                
        return -1
        