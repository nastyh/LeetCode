from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        """
        O(n), num of queries
        O(limit+c), c is the num of distinct colors (it's for the dicts)
        map ball labels to the current colors in ball_colors
        color_count track how many balls have each color
        If the ball already had a color, reduce the count of the old color.
        If the old color count becomes 0, remove it from the distinct count.
        Add the new color to the count and update the mapping.
        Track the distinct color count after each query and add to res
        """
        res = []
        ball_colors, color_count = {}, {}
        dist_color_count = 0
        for ball, color in queries:
            if ball in ball_colors:
                old_color = ball_colors[ball]
                if old_color in color_count:
                    color_count[old_color] -= 1
                    if color_count[old_color] == 0:
                        dist_color_count -= 1
            ball_colors[ball] = color
            if color not in color_count or color_count[color] == 0:
                dist_color_count += 1  # New color introduced
            color_count[color] = color_count.get(color, 0) + 1
            res.append(dist_color_count)
        return res