import itertools

class AnagramChecker:
    def __init__(self, word_list_file):
        """
        Initialize the AnagramChecker with a list of valid words loaded from the provided word list file.
        """
        self.word_list = self.load_word_list(word_list_file)

    def load_word_list(self, word_list_file):
        """
        Load words from the provided file into a set for efficient lookup.
        """
        try:
            with open('anagrams.txt', 'r') as file:
                return set(word.strip().lower() for word in file if word.strip())
        except FileNotFoundError:
            print("Error: Word list file not found.")
            return set()

    def is_valid_word(self, word):
        """
        Check if a word is valid (exists in the word list).
        """
        return word.lower() in self.word_list

    def is_anagram(self, word1, word2):
        """
        Check if two words are anagrams.
        """
        return sorted(word1.lower()) == sorted(word2.lower()) and word1.lower() != word2.lower()

    def get_anagrams(self, word):
        """
        Find all anagrams for the given word.
        """
        return [word_candidate for word_candidate in self.word_list if self.is_anagram(word, word_candidate)]