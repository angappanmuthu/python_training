import time


class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) <= 15 and len(s) >= 1:
            ''''
                I
                II
                III
                IV
            '''
            symbol = {'I': 1, 'V': 5, 'X': 10,
                      'L': 50, 'C': 100, 'D': 500, 'M': 1000}
            if len(s) <= 2:
                if s[:2] == "IV":
                    return 4
                elif s[:2] == "IX":
                    return 9
                elif s[:2] == "IX":
                    return 9

            value = 0
            for i in s:
                value = value + symbol[i]
            return value

test = "XXIV"


start_time = time.time()
print(Solution().romanToInt(test))
print("--- %s seconds ---" % (time.time() - start_time))
