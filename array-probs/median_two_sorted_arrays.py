class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        m = nums1 + nums2
        m.sort()

        l = len(m)

        #print(l)
        if l == 1:
            return m[0]
        elif (l+1) % 2 == 0:

            return m[int((l+1)/2)-1]

        else:

            idx , idy = int((l+1)/2 - 0.5) , int((l+1)/2 + 0.5)

            return (m[idx - 1] + m[idy - 1]) / 2
