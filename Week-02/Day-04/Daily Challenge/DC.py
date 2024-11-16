class Text:
    def __init__(self, text):
        """
        Initialize the Text class with the given string.
        """
        self.text = text
        self.words = self.text.lower().split()  # Preprocess the text into words once

    def word_frequency(self, word):
        """
        Return the frequency of a word in the text.
        """
        count = self.words.count(word.lower())
        return count if count > 0 else f"The word '{word}' is not found in the text."

    def most_common_word(self):
        """
        Return the most common word in the text.
        """
        if not self.words:
            return "The text is empty."
        from collections import Counter
        word_counts = Counter(self.words)
        most_common, count = word_counts.most_common(1)[0]
        return f"The most common word is '{most_common}', which appears {count} times."

    def unique_words(self):
        """
        Return a list of all unique words in the text.
        """
        return sorted(set(self.words))  # Sorted list for consistency

    @classmethod
    def from_file(cls, filename):
        """
        Create a Text instance from a text file.
        """
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
            return cls(content)
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
            return None


# Part I: Analyze a simple string
text_instance = Text("A good book would sometimes cost as much as a good house.")

# Testing the methods
print(text_instance.word_frequency("good"))  # Expected Output: 2
print(text_instance.most_common_word())      # Expected Output: The most common word is 'a', which appears 3 times.
print(text_instance.unique_words())          # Expected Output: ['a', 'as', 'book', 'cost', 'good', 'house', 'much', 'sometimes', 'would']

# Part II: Analyze a text file
file_text_instance = Text.from_file("the_stranger.txt")
if file_text_instance:
    print(file_text_instance.word_frequency("the"))  # Example output: 100 (depends on file content)
    print(file_text_instance.most_common_word())     # Example output: The most common word is 'the', which appears 100 times.
    print(file_text_instance.unique_words())         # Expected Output: A sorted list of unique words in the file.