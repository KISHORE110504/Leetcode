"""You are given a 2D binary array grid. You need to find 3 non-overlapping rectangles having non-zero areas with horizontal and vertical sides such that all the 1's in grid lie inside these rectangles.
Return the minimum possible sum of the area of these rectangles.
Note that the rectangles are allowed to touch.
"""
from typing import List

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def rect_area(r1, c1, r2, c2):
            """Get area & whether this subgrid has any 1"""
            has_one = False
            min_r, max_r, min_c, max_c = m, -1, n, -1
            for i in range(r1, r2):
                for j in range(c1, c2):
                    if grid[i][j] == 1:
                        has_one = True
                        min_r = min(min_r, i)
                        max_r = max(max_r, i)
                        min_c = min(min_c, j)
                        max_c = max(max_c, j)
            if not has_one:
                return None
            return (max_r - min_r + 1) * (max_c - min_c + 1)

        INF = float("inf")
        ans = INF

        # Case 1: 3 vertical stripes
        for c1 in range(1, n - 1):
            for c2 in range(c1 + 1, n):
                a1 = rect_area(0, 0, m, c1)
                a2 = rect_area(0, c1, m, c2)
                a3 = rect_area(0, c2, m, n)
                if a1 and a2 and a3:
                    ans = min(ans, a1 + a2 + a3)

        # Case 2: 3 horizontal stripes
        for r1 in range(1, m - 1):
            for r2 in range(r1 + 1, m):
                a1 = rect_area(0, 0, r1, n)
                a2 = rect_area(r1, 0, r2, n)
                a3 = rect_area(r2, 0, m, n)
                if a1 and a2 and a3:
                    ans = min(ans, a1 + a2 + a3)

        # Case 3: vertical cut, then horizontal cut on right
        for c in range(1, n):
            for r in range(1, m):
                a1 = rect_area(0, 0, m, c)
                a2 = rect_area(0, c, r, n)
                a3 = rect_area(r, c, m, n)
                if a1 and a2 and a3:
                    ans = min(ans, a1 + a2 + a3)

        # Case 4: vertical cut, then horizontal cut on left
        for c in range(1, n):
            for r in range(1, m):
                a1 = rect_area(0, c, m, n)
                a2 = rect_area(0, 0, r, c)
                a3 = rect_area(r, 0, m, c)
                if a1 and a2 and a3:
                    ans = min(ans, a1 + a2 + a3)

        # Case 5: horizontal cut, then vertical cut on bottom
        for r in range(1, m):
            for c in range(1, n):
                a1 = rect_area(0, 0, r, n)
                a2 = rect_area(r, 0, m, c)
                a3 = rect_area(r, c, m, n)
                if a1 and a2 and a3:
                    ans = min(ans, a1 + a2 + a3)

        # Case 6: horizontal cut, then vertical cut on top
        for r in range(1, m):
            for c in range(1, n):
                a1 = rect_area(r, 0, m, n)
                a2 = rect_area(0, 0, r, c)
                a3 = rect_area(0, c, r, n)
                if a1 and a2 and a3:
                    ans = min(ans, a1 + a2 + a3)

        return ans if ans != INF else -1
