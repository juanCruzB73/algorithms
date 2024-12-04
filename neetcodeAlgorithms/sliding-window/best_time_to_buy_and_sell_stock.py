class Solution:
    def maxProfit(prices: list[int]) -> int:
        profit=0
        i=0
        j=1
        while(j<len(prices)):
            if(prices[i]>prices[j]):
                i+=1
                continue
            total=prices[j]-prices[i]
            if(total>profit):
                profit=total
                print(profit)
            j+=1
        return profit


prices = [10,1,5,6,7,1]
prices2=[2,1,2,1,0,1,2]
result=Solution.maxProfit(prices2)
print(result)