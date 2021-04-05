# -*- coding: utf-8 -*-
__author__ = '陈章'
__date__ = '2021/4/5 23:35'
"""
你在和朋友一起玩 猜数字（Bulls and Cows）游戏，该游戏规则如下：

你写出一个秘密数字，并请朋友猜这个数字是多少。
朋友每猜测一次，你就会给他一个提示，告诉他的猜测数字中有多少位属于数字和确切位置都猜对了（称为“Bulls”, 公牛），有多少位属于数字猜对了但是位置不对（称为“Cows”, 奶牛）。
朋友根据提示继续猜，直到猜出秘密数字。
请写出一个根据秘密数字和朋友的猜测数返回提示的函数，返回字符串的格式为 xAyB ，x 和 y 都是数字，A 表示公牛，用 B 表示奶牛。

xA 表示有 x 位数字出现在秘密数字中，且位置都与秘密数字一致。
yB 表示有 y 位数字出现在秘密数字中，但位置与秘密数字不一致。
请注意秘密数字和朋友的猜测数都可能含有重复数字，每位数字只能统计一次。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bulls-and-cows
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
题目看了半小时，愣是没看懂。然后看了题解，给了两种方式。一种是要遍历两次。第一次，把数字出现的次数放在对应的两个数组里面，然后对相同索引的
数组的最小值求和。 
第二种是只用一个数组，每次遇到secret的话给数组位置+1， 遇到guess的话给数组位置-1。 如果加减之前发现secret的字母位置小于0，证明字母在guess
当中出现过，给奶牛+1， 如果guess的字母的位置大于0，证明字母在secret中出现过，给奶牛+1.
不是很好理解。 感觉最好的题解是  https://leetcode-cn.com/problems/bulls-and-cows/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by--55/
要多看看才能理解。
"""


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        l = [0 for i in range(10)]
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                secretInt = ord(secret[i]) - ord('0')
                guessInt = ord(guess[i]) - ord('0')
                if l[secretInt] < 0:
                    cows += 1
                if l[guessInt] > 0:
                    cows += 1
                l[secretInt] += 1
                l[guessInt] -= 1
        return f"{bulls}A{cows}B"
