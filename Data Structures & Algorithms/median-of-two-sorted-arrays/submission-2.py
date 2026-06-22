class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []
        # sort the array
        i = 0
        j = 0
        while i < len(nums1) or j < len(nums2):
            if len(nums1) <= i or j >= len(nums2):
                break
            smaller = min(nums1[i], nums2[j])
            res.append(smaller)
            if smaller == nums1[i]:
                i +=1
            else:
                j+=1
        
        for x in range(i, len(nums1)):
            res.append(nums1[x])
        for x in range(j, len(nums2)):
            res.append(nums2[x])

        print(res)
        
        # calculate the median
        median = float("-inf")
        n = len(res)
        if n % 2 == 0:
            first_term = res[(n // 2) - 1]
            scnd_term = res[(n // 2)]
            median = ( first_term + scnd_term ) / 2
        else:
            median = res[(n//2)]
        return median
            
        


