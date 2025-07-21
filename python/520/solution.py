class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        if(word[0].isupper()):
            if(len(word) == 1):
                return True
            if(word[1].isupper()):
                expectedPattern = "UPPER"
            else:
                expectedPattern = "Camel"
        else:
            expectedPattern = "lower"

        for char in word[1:]:
            if(char.isupper()):
                if(expectedPattern != "UPPER"):
                    return False
            else:
                if(expectedPattern == "UPPER"):
                    return False
        return True