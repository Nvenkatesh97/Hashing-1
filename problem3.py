class Solution:
    def wordPattern(self, pattern, text):
        words = text.split()
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, words):
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                char_to_word[char] = word

            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char

        return True


if __name__ == "__main__":
    
    sol = Solution()


    print(sol.wordPattern("abba", "dog cat cat dog"))    
    print(sol.wordPattern("abba", "dog cat cat fish"))    
    print(sol.wordPattern("aaba", "dog cat cat dog"))     
    print(sol.wordPattern("aaaa", "dog dog dog dog"))    
