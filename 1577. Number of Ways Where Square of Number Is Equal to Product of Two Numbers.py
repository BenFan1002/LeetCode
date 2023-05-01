class Solution(object):
    def helper(self, nums1, nums2):
        count = 0
        freq = {}
        for num in nums1:
            i = num * num
            freq[i] = freq.get(i, 0) + 1
        for j in range(len(nums2)):
            for k in range(j):
                product = nums2[j] * nums2[k]
                if product in freq:
                    count += freq[product]
        return count

    def numTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        return self.helper(nums1, nums2) + self.helper(nums2, nums1)


if __name__ == '__main__':
    print(Solution().numTriplets([1, 1], [1, 1, 1]))
