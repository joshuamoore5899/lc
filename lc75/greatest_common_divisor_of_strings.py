'''
1071. Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and 
only if s = t + t + t + ... + t + t (i.e., t is concatenated 
with itself one or more times).

Given two strings str1 and str2, return the largest 
string x such that x divides both str1 and str2.
'''

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        smallest = str1 if len(str1) <= len(str2) else str2
        smallest_original = smallest
        biggest = str1 if smallest == str2 else str2

        while len(smallest) > 0:
            n = len(biggest) // len(smallest)
            m = len(smallest_original) // len(smallest)
            if smallest * n == biggest and smallest * m == smallest_original:
                return smallest
            smallest = smallest[:-1]
        
        return ''