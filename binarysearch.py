def functionget(arr,target):
	low=0;
	high=len(arr)-1
	if(low>high):
		return -1
	mid=(low+high)//2
	if arr[mid]==target:
		return mid
	elif arr[mid]>target:
		return functionget(arr,target,mid-1,low)
	else:
		return functionget(arr,target,high,mid-1)


listed=[1,2,34,67,89,123,1234,4000]

result=functionget(listed,123)