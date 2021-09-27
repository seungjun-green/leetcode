'''
* at htere time complexity of solution1 and solution2 both are o(n).
But Solution 1 is ~7 times faster than Solution 2. Why??

if we define number of sapce as 'k'

Solution 1 : O(n) + O(k) -> O(n) (bc K is constant)
Solution 2: (k+1)(2*O(n))

So Solution 1 is faster!!!



'''


# Solution 1/2
'''
Time Complexity: O(n)
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        list1 = []
        result = []
        list1 = s.split(' ') # O(n)
        
        for i in range(len(list1)):
            a = list1[i]
            result.append(a[::-1]) #O(n)
            
        return " ".join(result)
      
      
# Solution 2/2
# Time Complexity: O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        temp = []
        result = []
        ans = ""
        for i in range(len(s)):
            if s[i] != ' ':
                temp.append(s[i])
            if s[i] == ' ' or i == (len(s) - 1):
                temp.reverse() #O(n)
                a = "".join(temp) #O(n)
                result.append(a)
                temp = []
              
        print(result)    
                
        return " ".join(result)
            
