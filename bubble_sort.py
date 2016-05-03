arr=[]
import random
for i in range(0,10):
    arr.append(int(random.random()* 10000))
print arr

x = 0
for x in range(0,len(arr)-1):    
    for i in range(0,len(arr)-1):
        if arr[i] > arr[i+1]:
            x = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = x
        
print arr


