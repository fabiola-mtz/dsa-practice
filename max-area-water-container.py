"""
    You are given an integer array height of length n. 
    There are n vertical lines drawn such that the two 
    endpoints of the ith line are (i, 0) and (i, height[i]).
"""

def max_area(heights):
    l = 0
    r = len(heights) - 1
    water = 0

    while l < r:
        x = r - l
        if heights[l] < heights[r]:
            area = x * heights[l]
            l += 1
        else:
            area = x * heights[r] 
            r -= 1

        if area > water:
            water = area
            
    return water