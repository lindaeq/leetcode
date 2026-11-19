class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        # edge case: if ch not in word
        if ch not in word:
            return word
        result = []
        
        # first ch occurrence
        index = 0
        for i in range(len(word)):
            if word[i] == ch:
                index = i
                break
        
        # append characters in rev from index down to 0
        for x in range(index, -1, -1):
            result.append(word[x])
            
        # add the rest of the word again after index
        for y in range(index + 1, len(word)):
            result.append(word[y])
            
        return "".join(result)