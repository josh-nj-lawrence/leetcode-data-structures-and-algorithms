from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = defaultdict(int)
        for c in text:
            counts[c] += 1
        balloonCounts = []
        for x in "balloon":
            if x == "l" or x == "o":
                balloonCounts.append(counts[x]//2)
            balloonCounts.append(counts[x])
        return min(balloonCounts)

solution = Solution()
print(solution.maxNumberOfBalloons("krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"))

# Results: 34.1% time (46ms) 45.38% space (14mb)