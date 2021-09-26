class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        hashmap = {}
        for i in range(len(nums1)):
            if nums1[i] not in hashmap:
                hashmap[nums1[i]] = 1
            else:
                hashmap[nums1[i]] += 1
                
        result = []
        for i in range(len(nums2)):
            if nums2[i] in hashmap and hashmap[nums2[i]] > 0:
                result.append(nums2[i])
                hashmap[nums2[i]] -=1
                
        return result
