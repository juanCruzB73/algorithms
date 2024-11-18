'''
You are given an array non-negative integers heights which represent an elevation map.

Each value heights[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.
'''

def trap(height: list[int]) -> int:
    result=0
    p1, p2 = 0,len(height)-1
    max_left,max_right=height[p1],height[p2]
    while(p1<p2):

        if(max_left<height[p1]):
            max_left=height[p1]
        
        if(max_right<height[p2]):
            max_right=height[p2]
        
        if(max_left<max_right):
            result+=max_left-height[p1]
            p1 += 1
        else:
            result+=max_right-height[p2]
            p2-=1
            
    return result

height = [0,2,0,3,1,0,1,3,2,1]
result=trap(height)
print(result)