from merge_strings_alternately import Solution

def test_merge_strings_alternately():
    strings = Solution()
    assert strings.mergeAlternately("abc", "def") == "adbecf"
    assert strings.mergeAlternately("short", "longerword") == "slhoonrgterword"
    assert strings.mergeAlternately("longer", "tiny") == "ltoinngyer"
    assert strings.mergeAlternately("", "test") == "test"