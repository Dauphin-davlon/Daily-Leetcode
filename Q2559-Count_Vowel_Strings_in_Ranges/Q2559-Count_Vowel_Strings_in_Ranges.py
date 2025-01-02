class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # declare a varibale for the prefix sum
        prefixSum = [0] * (len(words) + 1) 
        #create a list for vowels
        vowels = ["a","e","i","o","u"]
        # declare a varaible for sum
        sum = 0
        # loop through the words 
        for i, word in enumerate(words):
            # if the fit the requirement, we add 1 to sum
            if word[0] in vowels and word[-1] in vowels:
                sum += 1
            #  make the prefix sum[i] to be sum
            prefixSum[i] = sum

        # append 0 to the prefix sum
        prefixSum[len(words)] = 0

        # declare a varaible for result list
        result = [0] * len(queries)

        #loop through the queries
        for i, query in enumerate(queries):
            # subtact the right of the query in the prefix sum from one before the left in the prefix sum
            result[i] = prefixSum[query[1]] - prefixSum[query[0] - 1]
        
        #return the result
        return result

        