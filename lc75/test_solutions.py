from merge_strings_alternately import Solution as S1
from greatest_common_divisor_of_strings import Solution as S2
from kids_with_the_greatest_number_of_candies import Solution as S3

def test_merge_strings_alternately():
    strings = S1()
    assert strings.mergeAlternately("abc", "def") == "adbecf"
    assert strings.mergeAlternately("short", "longerword") == "slhoonrgterword"
    assert strings.mergeAlternately("longer", "tiny") == "ltoinngyer"
    assert strings.mergeAlternately("", "test") == "test"

def test_greatest_common_divisor_of_strings():
    strings = S2()
    assert strings.gcdOfStrings("abcabc", "abc") == "abc"
    assert strings.gcdOfStrings("abcabca", "abc") == ""
    assert strings.gcdOfStrings("abcabc", "abcabc") == "abcabc"
    assert strings.gcdOfStrings("abab", "ababab") == "ab"
    assert strings.gcdOfStrings("1234567", "123456712345671234567") == "1234567"

def test_kids_with_the_greatest_number_of_candies():
    strings = S3()
    assert strings.kidsWithCandies([1,2,3], 4) == [True, True, True]
    assert strings.kidsWithCandies([1,2,3], 1) == [False, True, True]
    assert strings.kidsWithCandies([4,8,3,7,5], 2) == [False, True, False, True, False]