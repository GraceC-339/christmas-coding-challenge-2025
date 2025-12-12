# 784. Letter Case Permutation
# Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
# Return a list of all possible strings we could create. You can return the output in any order.

from typing import List
class LetterCasePermutationSolution:
    def letterCasePermutation(self, s: str) -> List[str]:
        output = [""]

        for char in s:
            tmp = []
            if char.isalpha():
                for o in output:
                    tmp.append(o + char.lower())
                    tmp.append(o + char.upper())
            else:
                for o in output:
                    tmp.append(o + char)
            output = tmp
        
        return output
# Solution:
# We use an iterative approach to build all possible permutations of the input string.
# For each character in the string, if it's a letter, we create two new permutations for each existing permutation:
# one with the letter in lowercase and one with it in uppercase. If it's not a letter, we simply append it to each existing permutation.
# Time Complexity: O(2^m * n), where m is the number of letters in the string and n is the length of the string.
# Space Complexity: O(2^m * n) for storing the output


