from typing import List

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ones = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1]
        
        if not ones:
            return 0  # no 1s, no rectangles needed
        
        def rect_area(points):
            if not points:
                return 0
            min_r, max_r = min(r for r, _ in points), max(r for r, _ in points)
            min_c, max_c = min(c for _, c in points), max(c for _, c in points)
            return (max_r - min_r + 1) * (max_c - min_c + 1)

        best = float('inf')
        
        # Try horizontal cuts (split into 3 horizontal bands)
        for r1 in range(m-2):
            for r2 in range(r1+1, m-1):
                group1 = [(i,j) for i,j in ones if i <= r1]
                group2 = [(i,j) for i,j in ones if r1 < i <= r2]
                group3 = [(i,j) for i,j in ones if i > r2]
                best = min(best, rect_area(group1)+rect_area(group2)+rect_area(group3))
        
        # Try vertical cuts (split into 3 vertical bands)
        for c1 in range(n-2):
            for c2 in range(c1+1, n-1):
                group1 = [(i,j) for i,j in ones if j <= c1]
                group2 = [(i,j) for i,j in ones if c1 < j <= c2]
                group3 = [(i,j) for i,j in ones if j > c2]
                best = min(best, rect_area(group1)+rect_area(group2)+rect_area(group3))
        
        return best
