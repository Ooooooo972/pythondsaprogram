def pairtwosum(arr,traget):
  for i in range (len(arr)):
    for j in range (i+1,len(arr)):
      if arr[i]+arr[j]==traget:
        return [i,j]
  return []

arr=[2,8.9,5,3,1]
traget=4
print(pairtwosum(arr,traget))