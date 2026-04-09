class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        n = len(nums1)
        for i in range(n):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    k = j+1
                    found = False
                    while k < len(nums2):
                        if nums2[k] > nums2[j]:
                            res.append(nums2[k])
                            found = True
                            break
                        else:
                            k+=1
                    if not found:
                        res.append(-1)
                    break
        return res 


