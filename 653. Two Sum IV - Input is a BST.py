'''
Algorihtm:
1. iterating the BST, create a hashmap
2. iterating the hashmap, get the complement and check whether complement != key and complement is in hashmap, if its true, return True
3. after iteration of hashmap, if True was not returend, return False
'''
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hashmap = {}
        if root is None:
            return False
        self.record(root, hashmap)
        print(hashmap)
        
        for key in hashmap:
            complement = k - key
            if complement in hashmap and complement != key:
                return True
            
        
        return False
        
    
    def record(self, root, hashmap):
        if root.val not in hashmap:
            hashmap[root.val] = 1
            
            if root.right is not None:
                self.record(root.right, hashmap)
            
            if root.left is not None:
                self.record(root.left, hashmap)
