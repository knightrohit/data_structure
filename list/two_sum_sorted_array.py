""" 
Add sorted array elements to produce a target result 
Input = [0,0,3,4], target = 0
Output = [1, 2], here index starts with 1 and not 0
"""
def test(numbers, target):

    if not numbers or target == None:
        return []
    
    p1 = 0
    p2 = len(numbers) - 1
    while p1 < p2:
        sum_val = numbers[p1] + numbers[p2]
        print(sum_val, p1, p2)
        if sum_val == target:
            return [p1 + 1, p2 + 1]
        
        elif sum_val > target:
            p2 -= 1
            
        else:
            p1 += 1
            
    return []


print(test([0,0,3,4], 0))