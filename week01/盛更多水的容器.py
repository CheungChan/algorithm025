# -*- coding: utf-8 -*-
__author__ = '陈章'
__date__ = '2021/4/5 13:12'

# 盛更多水的容器。双指针法夹逼。
# 当i，j为最左和最右的时候底是最大的，此时无论是i++还是j--，底是一样的，都是减1。如果移动更低的指针，那么
# 容器的高才尽可能的大。
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        maxA = 0
        while (i < j):
            maxA = max(maxA, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxA
