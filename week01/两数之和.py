# -*- coding: utf-8 -*-
__author__ = '陈章'
__date__ = '2021/4/5 13:15'
# 两数之和，使用map缓存之前遍历的数和索引。只遍历一次，用空间换时间。
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, n in enumerate(nums):
            if n in d:
                return [d[n], i]
            else:
                d[target - n] = i
        return [-1, -1]
