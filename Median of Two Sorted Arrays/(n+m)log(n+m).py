class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # first merge two array
        # then sort it
        # then find the middle point, dividied in two cases, len is odd and when len is even
        
        
        merged = nums1 + nums2
        
        result = self.merge_sort(merged)
        half = len(result) // 2
        
        if len(result) % 2 == 0:
            return (result[half] + result[half -1]) /2
        else:
            return result[half]
        
  
        
    def merge_sort(self, list):
    
        #base case
        if len(list) <= 1:
            return list
        #recursive case
        else:
        
            middle_index = len(list)//2
        
            left_half = self.merge_sort(list[middle_index:])
            right_half = self.merge_sort(list[:middle_index])
        
            sorted_list = []
    
            left_index = 0
            right_index = 0
        
            #get sorted_list, combinging left_half and right_half in ascending order
            while left_index < len(left_half) and right_index < len(right_half):
                if left_half[left_index] <= right_half[right_index]:
                    sorted_list.append(left_half[left_index])
                    left_index += 1
                else:
                    sorted_list.append(right_half[right_index])
                    right_index += 1
                
            sorted_list += left_half[left_index:]
            sorted_list += right_half[right_index:]
            return sorted_list
        
        
        
        
        
        
        
