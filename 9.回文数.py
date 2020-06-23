#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        str_x = str(x)
        i = 0
        while i < len(str_x)-i:
            if str_x[i] != str_x[-i]:
                return False
            i = i+1
        
        return True

# @lc code=end

