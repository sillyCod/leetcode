#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        i = 0
        while True:

            init = self.gen_node()
            for item in strs:
                try:
                    index = ord(item[i])-97
                    # if init[index] == 0:
                    init[index] = 1
                    if len(list(filter(lambda i: i, init))) > 1:
                        print("current i is ", i)
                        return strs[0][0:i]

                except IndexError:
                    return item
            i+=1
        # return strs[0:i]
            


    def gen_node(self):
        return [0 for i in range(26)]
# @lc code=end


