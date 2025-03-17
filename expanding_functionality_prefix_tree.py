from trie import Trie


class Homework(Trie):
    def count_words_with_suffix(self, pattern: str) -> int:
        return sum(1 for key in self.keys() if key.endswith(pattern))

    def has_prefix(self, prefix: str) -> bool:
        return any(key.startswith(prefix) for key in self.keys())


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat", "lemon"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Check if the word is ending with the given suffix
    assert trie.count_words_with_suffix("e") == 1  # apple
    print(trie.count_words_with_suffix("e"))
    assert trie.count_words_with_suffix("ion") == 1  # application
    print(trie.count_words_with_suffix("ion"))
    assert trie.count_words_with_suffix("a") == 1  # banana
    print(trie.count_words_with_suffix("a"))
    assert trie.count_words_with_suffix("at") == 1  # cat
    print(trie.count_words_with_suffix("at"))
    assert trie.count_words_with_suffix("on") == 2  # application, lemon
    print(trie.count_words_with_suffix("on"))

    # Check if the word has the given prefix
    assert trie.has_prefix("app") == True  # apple, application
    print(trie.has_prefix("app"))
    assert trie.has_prefix("bat") == False
    print(trie.has_prefix("bat"))
    assert trie.has_prefix("ban") == True  # banana
    print(trie.has_prefix("ban"))
    assert trie.has_prefix("ca") == True  # cat
    print(trie.has_prefix("ca"))

    print("All tests passed.")
