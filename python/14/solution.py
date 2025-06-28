from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs) == 1):
            return strs[0]
        elif ("" in strs):
            return ""
        prefix = ""
        characterIndex = 0
        maximumCharacters =  len(max(strs, key=len))

        while characterIndex < (maximumCharacters):
            wordIndex = 0
            lst = []
            while wordIndex < len(strs):
                if(characterIndex + 1 > len(strs[wordIndex])):
                    return prefix
                lst.append(strs[wordIndex][characterIndex])
                wordIndex+=1
            if (lst[:-1] == lst[1:]):
                prefix += lst[0]
                characterIndex+=1
            else:
                return prefix


sol = Solution()
print(sol.longestCommonPrefix(["abca", "abc"]))