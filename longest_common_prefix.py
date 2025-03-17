from trie import Trie


class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if strings is None or len(strings) == 0:
            return ""

        prefix = strings[0]
        for string in strings[1:]:
            while string.startswith(prefix) is False:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix


if __name__ == "__main__":
    # Tests
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"
    # print(trie.find_longest_common_word(strings))

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"
    # print(trie.find_longest_common_word(strings))

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""
    # print(trie.find_longest_common_word(strings))

    print("All tests passed!")
