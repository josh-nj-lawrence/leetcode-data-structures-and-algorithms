from typing import List
class Solution:
    def reverseWords(self, s: str) -> str:
        input = s.split()
        for i,word in enumerate(input):
            new_word=[""]*len(word)
            l,r = 0,len(word)-1
            while l<=r:
                if l<r:
                    new_word.insert(r,word[l])
                    new_word.insert(l, word[r])
                else:
                    # Equal case
                    new_word.insert(l,word[r])
                l+=1
                r-=1
            input[i] = "".join(new_word)
        return " ".join(input)
solution = Solution()
print(solution.reverseWords("Let's take LeetCode contest"))

# Results: God aweful 5.1% speed (256 ms) 11.46% space (14.7 MB)
    
class OfficialSolution:
    def reverseWords(self, s: str) -> str:
        lastSpaceIndex: int = -1
        chArray: chr[List] = list(s)
        length: int = len(chArray)
        for strIndex in range(length):
            if strIndex == length or s[strIndex] == ' ':
                startIndex: int = lastSpaceIndex + 1
                endIndex: int = strIndex -1
                while startIndex < endIndex:
                    temp: chr = chArray[startIndex]
                    chArray[startIndex] = chArray[endIndex]
                    chArray[endIndex] = temp
                    startIndex += 1
                    endIndex -= 1
                lastSpaceIndex = strIndex
        return "".join(chArray)
solution2 = OfficialSolution()
print(solution2.reverseWords("Let's take LeetCode contest"))

# Seems to have an issue
