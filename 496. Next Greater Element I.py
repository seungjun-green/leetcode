'''
Time Complexity: O(n ^ 2)

Algorithms:
1. create a hashmap of nums, key as nums2[i], and value as i
2. Iterating nums1, find the index of nums1[i] in nums2 => k
3. in nums2 from index k to last index, if there is element bigger than nums1[i], append the element to result list, otherwisr append -1 to the result list
4. return the list after end of iteration of nums1

'''

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        result = []
        hashmap = {}
        for i in range(len(nums2)):
            hashmap[nums2[i]] = i
        
        for i in range(len(nums1)):
            k = hashmap[nums1[i]]
            for j in range(k, len(nums2)):
                if nums2[j] > nums1[i]:
                    result.append(nums2[j])
                    break
                    
            if len(result) != i + 1:
                result.append(-1)
        
        return result
                
        
