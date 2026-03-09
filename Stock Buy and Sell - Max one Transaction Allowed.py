def maxprofit(prices):
   n=len(prices)
   rees=0
   for i in range (0,n):
     for j in range (i+1,n):
       if prices[j]>prices[i]:
         rees=max(rees,prices[j]-prices[i])
   return rees
prices=[7,1,5,3,6,4]
print(maxprofit(prices))