class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Idea 1: 2 Pointers
        # Idea 2: Merge Sort
        # Idea 3: Swap element in that's smaller
        # Idea 4: Start greatest to smallest

        p1, p2, pos = m - 1, n - 1, m + n - 1 # setting each pointer to the end of their array

        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[pos] = nums1[p1]
                p1 -= 1
            else:
                nums1[pos] = nums2[p2]
                p2 -= 1
            pos -= 1
        