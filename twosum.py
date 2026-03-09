def twosum(arr,target):
  n=len(arr)
  hashmap={}
  for i in range (0,n):
    if target-arr[i] in hashmap:
      return [hashmap[target-arr[i]],i]
    hashmap[arr[i]]=i
  return []


arr=[2,5,9,5,3,1]
target=10     
print(twosum(arr,target))