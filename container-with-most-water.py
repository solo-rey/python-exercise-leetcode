
# @return an integer
def maxArea(height):
    if not height or len(height) == 0:
        return 0
    maxsize = 0
    low = 0
    high = len(height) - 1
    while low < high:
        size = (high-low) * min(height[low],height[high])
        maxsize = max(maxsize,size)
        if height[low] < height[high]:
            low+=1
        else:
            high-=1
    return maxsize
