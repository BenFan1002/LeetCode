from typing import List


class Solution(object):
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        pos = [0] * (m * n + 1)
        for i, row in enumerate(mat):
            for j, val in enumerate(row):
                pos[val] = (i, j)

        row = [0] * m
        col = [0] * n
        for i, v in enumerate(arr):
            r, c = pos[v]
            row[r] += 1
            col[c] += 1
            if row[r] == n or col[c] == m:
                return i


if __name__ == '__main__':
    print(Solution().firstCompleteIndex([2, 8, 7, 4, 1, 3, 5, 6, 9], [[3, 2, 5], [1, 4, 6], [8, 7, 9]]))
