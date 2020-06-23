#
# @lc app=leetcode.cn id=371 lang=python3
#
# [371] 两整数之和
#

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        a_bin = bin(a)
        b_bin = bin(b)
        if a_bin.startswith("-") ^ b_bin.startswith("-"):
            if a_bin.startswith("-"):
                a = bin(~a)
                addtional ="1"
                for i in reversed(a):
                    if i == "0":
                        
                



        
# @lc code=end

