class Solution:
    def longestConsecutive(self, nums):

        # Convert list to set for O(1) lookup
        numSet = set(nums)

        # Store longest sequence length found
        longest = 0

        # Check every number
        for n in numSet:

            # Is n the start of a sequence?
            if (n - 1) not in numSet:

                length = 0

                # Keep moving forward
                while (n + length) in numSet:
                    length += 1

                # Update answer
                longest = max(longest, length)

        return longest