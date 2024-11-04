class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        i = 0
        while i < len(word):
            count = 1
            while i + count < len(word) and word[i] == word[i+count] and count < 9:
                count += 1
            comp += str(count) + word[i]
            i += count
        return comp
