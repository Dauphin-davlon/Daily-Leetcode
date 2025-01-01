class Solution:
    def maxScore(self, s: str) -> int:
        
        #initialize variable for ones to 0
        ones = 0
        #initialize variable for zeros to 0
        zeros = 0
        #initialize variable for score to -inf
        score = -inf

        #loop through s (stop at index before the last one)
        for i in range(len(s) - 1):
            #if the current char is 1, then we increse count of one
            if s[i] == "1":
                ones += 1
            #if current cahr is 0, then increse zeros
            else:
                zeros += 1

            #calculate current max score = zeros - ones
            score = max(score, zeros - ones)

        #if the char at last index is 1, then increse ones
        if s[-1] == "1":
            ones += 1

        #return score + ones
        return score + ones
