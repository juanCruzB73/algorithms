'''
You are given an integer array heights where heights[i] represents the height of the ithith bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.
'''

#my answer
def maxArea(heights: list[int]) -> int:
    #height * len
    j,k=0,len(heights)-1
    current_max_area=0
    while(j<k):
        
        if(heights[j]<heights[k]):
            height=heights[j]
        else:
            height=heights[k]
        
        width=(k+1)-(j+1)

        aux_max_area=height*width
        
        if(aux_max_area>current_max_area):
            current_max_area=aux_max_area

        if(heights[j]<heights[k]):
            j+=1
        else:
            k-=1
    return current_max_area
        
          
height = [1,7,2,5,4,7,3,6]
result=maxArea(height)
print("result ",result)