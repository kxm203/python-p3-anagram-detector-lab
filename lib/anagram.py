class Anagram:

    def __init__ (self, word):
        self.word = word
    
    def match(self, word_list):
        anagrams = []
        for words in word_list:
            if sorted(words.lower()) == sorted(self.word.lower()) and words.lower() != self.word.lower():
                anagrams.append(words)
        return anagrams
