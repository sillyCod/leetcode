from collections import OrderedDict

class Solution:

    def romanToInt(self, s: str)->int:
        # max = 1
        # options = OrderedDict({
        #     "I": 1,
        #     "V": 5,
        #     "X": 10,
        #     "L": 50,
        #     "C": 100,
        #     "D":500,
        #     "M": 1000
        #     })
        # options_keys = list(options.keys())
        # options_reversed = sorted(options_keys, reverse=True)
        # for i in options_reversed:
        #     try:
        #         start = s.index(i)
        #         for j in range(start, len(s)):
        #             if s[j] != i:
        #                 end = j
        #                 break
        #         options[i] * (end-start) - self.roman_to_int(s[0:start]) + self.roman_to_int(s[end:])
        #     except ValueError as e:
        #         continue
        options = dict(I=1, V=5, IV=4, IX=9, X=10, XL=40, XC=90, C=100, CD=400, CM=900)
        result = 0
        i = 0

        while i < len(s):
            if options.get(s[i:i+2]):
                
                result += options[s[i:i+2]]
                i = i +2
            else:
                
                result += options[s[i:i+1]]
                i = i+1
        return result
            


