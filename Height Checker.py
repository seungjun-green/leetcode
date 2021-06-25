class Solution:
    unsorted_list = []
    sorted_list = []
    def heightChecker(self, unsorted_list):
        sorted_list = self.quick_sort(unsorted_list)
        dd = self.getAnswer(unsorted_list, sorted_list)
        return dd
        
    def getAnswer(self, unsorted_list, sorted_list):
        """
        compare each element
        """
        count = 0
        for i in range(0, len(sorted_list)):
            if unsorted_list[i] != sorted_list[i]:
                count += 1
    
        return count


    def quick_sort(self,list):
        #base case
        if len(list) == 0:
            return list
        
        #set the 3 sublists
        less_than_pivot = []
        bigger_than_pivot = []
        pivot = list[0]
    
        #recursive case
        for element in list[1:]:
            if element <= pivot:
                less_than_pivot.append(element)
            else:
                bigger_than_pivot.append(element)
        
        return self.quick_sort(less_than_pivot) + [pivot] + self.quick_sort(bigger_than_pivot)
    

a = Solution()

a.heightChecker([1,1,4,2,1,3])
    
    
    
            
