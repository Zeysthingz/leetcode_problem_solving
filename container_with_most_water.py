# 11. Container With Most Water
# Medium
# Topics
# Companies
# Hint
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.


TODO: Two pointer approach
# time execeeded
def maxArea(height):
    i = 0
    j = i + 1
    max_area = 0
    current_area = 0
    while (i < len(height) - 1 and j < len(height)):
        current_area = min(height[i], height[j]) * abs(i - j)
        if current_area >= max_area:
            max_area = current_area
        if j+1 != len(height):
            j += 1
        else:
            i += 1
            j = i + 1
    return max_area

def max_area(height):
    class Solution:
        def maxArea(self, height: List[int]) -> int:
            l = 0
            ans = 0
            h = len(height) - 1
            while l < h:
                a = min(height[l], height[h]) * (h - l)
                ans = max(a, ans)
                if height[l] < height[h]:
                    l += 1
                else:
                    h -= 1
