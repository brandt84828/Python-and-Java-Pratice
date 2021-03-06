# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 14:17:38 2018

@author: brand
"""

class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l, r = 0, len(A) - 1
        while l < r:
            mid = (l + r) // 2
            if A[mid] < A[mid + 1]:
                l = mid
            elif A[mid - 1] > A[mid]:
                r = mid
            else:
                return mid