'''
Time Complexity: O(1) - becasue limit of length of num is given in problem, time complexity is O(1) not O(n)
Algorithm

1.create roman hashmap

2. Converting the given num to way roman integer works, append each element in to a list called 'res'
(Ex- if num is 49 -> [10, 50, 1, 10])

3. iterating the list 'res', append the roman interger to the answer string.

'''

roman = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
}

class Solution:
    def intToRoman(self, num: int) -> str:
        res = []
        ans = ''
        nums = str(num)
        length = len(nums)
        for i in range(length):
            if nums[i] == '9':
                res.append(10**(length-i-1))
                res.append(10**(length-i))
            elif nums[i] == '4':
                res.append(10**(length-i-1))
                res.append(5*10**(length-i-1))
            else:
                if nums[i] == '5':
                    res.append(5*10**(length-i-1))
                elif int(nums[i]) > 5:
                    res.append(5*10**(length-i-1))
                    
                    for j in range(int(nums[i])-5):
                        res.append(10**(length-i-1))
                        
                else:
                    for j in range(int(nums[i])):
                        res.append(10**(length-i-1))
                                    
                
        for r in res:
            ans += roman[r]
            
        return ans
            
                
        
                
                
            
        
