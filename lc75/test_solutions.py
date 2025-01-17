from merge_strings_alternately import Solution as S1
from greatest_common_divisor_of_strings import Solution as S2

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
    assert strings.gcdOfStrings("123456", "123456123456123456") == "123456"