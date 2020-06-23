#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            origin = self.countAndSay(n-1)
            print("current origin is {}, index is {}".format(origin, n-1))
            index = 0
            char = origin[0]
            count = 1
            result = ""
            j = 0
            while index < len(origin):
                # for j in range(index, len(origin)):
                count = 1
                char = origin[index]
                print("j assign ", index)
                j = index
                while j < len(origin):
                    if origin[j] != char:
                        result = result + str(count)+char
                        char = origin[j]
                        index = j
                        break
                    else:
                        j = j+1
                        count = count + 1
                    print("count is ", count, char)
                
                break
                

            return result
            

# @lc code=end

